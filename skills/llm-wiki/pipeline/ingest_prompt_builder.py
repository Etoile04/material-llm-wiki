"""
标准化 Ingest Prompt 生成器。

根据论文特征生成标准化的 LLM ingest 任务 prompt。
避免手工 sessions_spawn 导致的不一致问题。
"""
import os, json

def build_ingest_prompt(slug, raw_path, wiki_root, has_formulas=True,
                       file_size_bytes=0, paper_type="pdf"):
    """
    Build standardized ingest prompt for LLM sub-agent.
    """
    if file_size_bytes > 60000:
        read_instruction = (
            f"⚠️ 文件较大 ({file_size_bytes//1024}KB)，使用 read 工具的 offset/limit 参数分批读取（每次 1500 行）\n"
            f"禁止一次性读取全文，否则子智能体会空跑退出"
        )
    else:
        read_instruction = f"读取完整文件（{file_size_bytes//1024}KB）"

    formula_section = ""
    if has_formulas:
        formula_section = """
## Key Equations (必须包含)

提取论文中的关键公式，使用 LaTeX 格式：
- 块级公式: $$...$$
- 行内公式: $...$
- 每个公式标注物理含义和变量说明
- 如果源文件缺公式，用 web_search 搜索论文 DOI 补充"""

    prompt = f"""你是核材料物理知识提取专家。使用 llm-wiki skill 的 ingest 操作导入论文。

## 论文信息
- Slug: {slug}
- 原始文件: {raw_path}
- 工作目录: {wiki_root}
- 文件类型: {paper_type}
- 包含公式: {'是' if has_formulas else '否'}

## 执行步骤

### Step 1: 读取源文件
{read_instruction}
⚠️ pdftotext 文件前 200 行可能是元数据，跳过

### Step 2: 生成中文摘要
创建: {wiki_root}/wiki/summaries/{slug}.md
- 200-400 词中文摘要
- 包含物理机制、关键参数、实验数据
{formula_section}

### Step 3: 提取结构化参数
创建: {wiki_root}/parameters/{slug}.json
- 遵循 schema_parameter.json 格式
- 提取 8 类参数：扩散系数、激活能、热力学、相变、弹性力学、辐照损伤、肿胀气泡、燃料性能
- 每类参数都应提取，即使论文主题不是肿胀
- 参数 ID 格式: {slug}_param_NNN

### Step 4: 运行 validate 检查
执行: python3 {wiki_root}/../skills/llm-wiki/scripts/validate_params.py {wiki_root}
确认: 该论文参数 0 FAIL

### Step 5: 记录日志
在 {wiki_root}/log/YYYYMMDD.md 中记录本次 ingest 结果

## 防重复规则
- 提取前先检查 paper_registry.json，避免重复 slug
- 如已存在则追加参数，不创建新文件

## 完成后报告
- Summary 文件路径和大小
- Parameters 文件路径和参数数量
- Validate 结果（PASS/FAIL）
"""
    return prompt

if __name__ == '__main__':
    p = build_ingest_prompt("2026_Test", "/tmp/test.md", "/wiki", True, 50000)
    print(p[:200])
    print(f"... Total: {len(p)} chars")
