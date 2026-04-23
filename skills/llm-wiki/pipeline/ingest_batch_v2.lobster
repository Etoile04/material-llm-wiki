name: ingest-batch
description: 批量论文 PDF转换 → 质量检查 → 报告

steps:
  - id: convert
    command: "python3 -c \"import os,sys; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','scripts')); import batch_convert; batch_convert.main()\""
