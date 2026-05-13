name: ingest-batch
description: 批量论文 PDF转换 → 质量检查 → 报告 (with resume checkpoint support)

steps:
  # ── Resume 检测：找出需要重新处理的论文 ──
  - id: resume_detect
    command: "python3 -c \"import json,sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from lobster_resume import CheckpointManager; cm=CheckpointManager(); resumable=cm.get_resumable(); print(json.dumps({'resumable_count':len(resumable),'resumable':resumable}))\""

  # ── 批量转换 ──
  - id: convert
    command: "python3 /Users/lwj04/.openclaw/workspace/data/fuel_swelling_wiki/pipeline/batch_convert.py"
    stdin: $resume_detect.stdout
