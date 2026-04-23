# Ingest Batch — Lobster Pipeline
# 批量导入论文到核材料知识库
#
# Usage:
#   lobster run path/to/ingest_batch.lobster
#   lobster run --file path/to/ingest_batch.lobster --args-json '{"pdfs":["/path/to/a.pdf","/path/to/b.pdf"]}'
#
# 环境变量:
#   WIKI_ROOT  — 知识库根目录 (默认: ./.. 即 data/fuel_swelling_wiki/)
#   VALIDATE_SCRIPT — 参数校验脚本路径
#   LINT_SCRIPT — wiki lint 脚本路径

# ── Step 0: 解析输入 & 准备环境 ─────────────────────────────
exec --shell "
  WIKI_ROOT=\"\${WIKI_ROOT:-$(dirname $(dirname $(realpath $0)))}\"
  echo \"{\\\"wiki_root\\\": \\\"\${WIKI_ROOT}\\\"}\"
" | json

# ── Step 1: 批量 Scan — 检查 PDF 有效性 & 提取元数据 ──────
exec --shell '
  WIKI_ROOT="${WIKI_ROOT:-$(dirname $(dirname $(realpath $0)))}"
  REPORT="/tmp/ingest_batch_report_$(date +%Y%m%d_%H%M%S).jsonl"
  > "$REPORT"

  for pdf in "$@"; do
    if [ ! -f "$pdf" ]; then
      echo "{\"slug\":\"$(basename $pdf .pdf)\",\"pdf_path\":\"$pdf\",\"status\":\"error\",\"reason\":\"file_not_found\"}" >> "$REPORT"
      continue
    fi
    # Extract page count and size for strategy selection
    pages=$(pdfinfo "$pdf" 2>/dev/null | grep Pages | awk "{print \$2}" || echo "999")
    size=$(stat -f%z "$pdf" 2>/dev/null || stat -c%s "$pdf" 2>/dev/null || echo 0)
    echo "{\"slug\":\"$(basename $pdf .pdf)\",\"pdf_path\":\"$pdf\",\"pages\":$pages,\"size_bytes\":$size,\"status\":\"scanned\"}" >> "$REPORT"
  done

  echo "{\"report_path\":\"$REPORT\"}"
' | json

# ── Step 2: PDF → Markdown (三层策略) ─────────────────────
exec --shell '
  WIKI_ROOT="${WIKI_ROOT:-$(dirname $(dirname $(realpath $0)))}"
  REPORT="$1"
  shift

  while IFS= read -r line; do
    pdf_path=$(echo "$line" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())[\"pdf_path\"])" 2>/dev/null)
    slug=$(echo "$line" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())[\"slug\"])" 2>/dev/null)
    pages=$(echo "$line" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get(\"pages\",999))" 2>/dev/null)
    size=$(echo "$line" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get(\"size_bytes\",0))" 2>/dev/null)

    out_dir="$WIKI_ROOT/raw/papers"
    mkdir -p "$out_dir"

    # 三层策略: flash-extract > extract > pdftotext
    if [ "$size" -lt 10485760 ] && [ "$pages" -lt 20 ]; then
      echo "{\"slug\":\"$slug\",\"strategy\":\"flash-extract\",\"status\":\"converting\"}" >> "$REPORT.conv"
      if mineru-open-api flash-extract "$pdf_path" -o "$out_dir/" --language en 2>/dev/null; then
        echo "{\"slug\":\"$slug\",\"strategy\":\"flash-extract\",\"status\":\"done\"}" >> "$REPORT.conv"
        continue
      fi
    fi

    echo "{\"slug\":\"$slug\",\"strategy\":\"pdftotext\",\"status\":\"converting\"}" >> "$REPORT.conv"
    pdftotext -layout "$pdf_path" "$out_dir/${slug}.txt" 2>/dev/null
    echo "{\"slug\":\"$slug\",\"strategy\":\"pdftotext\",\"status\":\"done\"}" >> "$REPORT.conv"
  done < "$REPORT"

  echo "{\"status\":\"all_converted\",\"report\":\"$REPORT.conv\"}"
' | json

# ── Step 3-5: 每篇论文 Spawn 子智能体执行 Summary + Parameters + Validate ──
# 这一步通过 sessions_spawn 为每篇论文启动独立子智能体，
# 子智能体按照 skills/llm-wiki/SKILL.md 的 ingest 流程执行：
#   3. Slug 验证 + 读取全文
#   4. 生成摘要 wiki/summaries/<slug>.md
#   5. 参数提取 parameters/<slug>.json
#
# 由于 Lobster pipeline 本身是 shell 管道，无法直接调用 sessions_spawn，
# 实际批量处理建议通过主智能体循环调用：
#
#   for each pdf:
#     sessions_spawn(
#       task="使用 llm-wiki skill 的 ingest 操作导入论文: {pdf_path}",
#       runtime="subagent", mode="run"
#     )
#
# 以下为参数校验步骤（所有摘要和参数生成完毕后执行）：

# ── Step 6: Validate — 参数质量验证 ────────────────────────
exec --shell '
  WIKI_ROOT="${WIKI_ROOT:-$(dirname $(dirname $(realpath $0)))}"
  VALIDATE_SCRIPT="${VALIDATE_SCRIPT:-$WIKI_ROOT/../skills/llm-wiki/scripts/validate_params.py}"

  if [ -f "$VALIDATE_SCRIPT" ]; then
    python3 "$VALIDATE_SCRIPT" "$WIKI_ROOT/parameters/"
  else
    # Fallback: basic JSON validation
    fail_count=0
    warn_count=0
    pass_count=0
    for f in "$WIKI_ROOT/parameters/"*.json; do
      [ -f "$f" ] || continue
      python3 -c "import json; json.load(open(\"$f\"))" 2>/dev/null
      if [ $? -eq 0 ]; then
        pass_count=$((pass_count + 1))
      else
        fail_count=$((fail_count + 1))
        echo "FAIL: $f — invalid JSON"
      fi
    done
    echo "{\"pass\":$pass_count,\"warn\":$warn_count,\"fail\":$fail_count}"
  fi
' | json

# ── Step 7: 质量门禁 — FAIL > 0 时暂停人工审核 ────────────
# 如果验证结果中 fail > 0，approve 节点会暂停等待人工确认
approve --prompt "参数验证完成。检查报告如上。FAIL 项需要人工审核后继续。是否继续？"

# ── Step 8: 生成批量报告 ──────────────────────────────────
exec --shell '
  WIKI_ROOT="${WIKI_ROOT:-$(dirname $(dirname $(realpath $0)))}"
  date_stamp=$(date +%Y%m%d)
  report_file="$WIKI_ROOT/log/batch_ingest_${date_stamp}.md"

  mkdir -p "$WIKI_ROOT/log"

  cat > "$report_file" << REPORT_EOF
# Batch Ingest Report — $(date +%Y-%m-%d)

## Summary

| Item | Count |
|------|-------|
| Summaries generated | $(ls "$WIKI_ROOT/wiki/summaries/"*.md 2>/dev/null | wc -l | tr -d " ") |
| Parameters extracted | $(ls "$WIKI_ROOT/parameters/"*.json 2>/dev/null | wc -l | tr -d " ") |
| Raw papers converted | $(ls "$WIKI_ROOT/raw/papers/"*.{md,txt} 2>/dev/null | wc -l | tr -d " ") |

## Files

### Summaries
$(ls "$WIKI_ROOT/wiki/summaries/"*.md 2>/dev/null | sed "s|$WIKI_ROOT/||" | while read f; do echo "- $f"; done || echo "(none)")

### Parameters
$(ls "$WIKI_ROOT/parameters/"*.json 2>/dev/null | sed "s|$WIKI_ROOT/||" | while read f; do echo "- $f"; done || echo "(none)")
REPORT_EOF

  echo "{\"report_file\":\"$report_file\"}"
' | json
