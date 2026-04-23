name: ingest-batch
description: 批量论文 PDF转换 → 质量检查 → 报告

steps:
  - id: convert
    command: "python3 /Users/lwj04/.openclaw/workspace/data/fuel_swelling_wiki/pipeline/batch_convert.py"
