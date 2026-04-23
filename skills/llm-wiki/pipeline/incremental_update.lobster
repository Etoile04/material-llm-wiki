name: incremental-update
description: 检测 Zotero 目录中新增 PDF，增量入库到知识库

steps:
  - id: detect
    description: 检测新增 PDF（与已有 raw/papers 和 summaries 比对）
    command: >-
      python3 -c "
      import glob, os, re, json, sys;
      wiki = os.environ.get('WIKI_ROOT', 'data/fuel_swelling_wiki');
      raws = set(os.path.basename(f).replace('.txt','')[:30] for f in glob.glob(f'{wiki}/raw/papers/*.txt'));
      summaries = set();
      [summaries.add((re.findall(r'[a-z]+', os.path.basename(f).lower())[0], re.findall(r'(19|20)\d{2}', os.path.basename(f))[0] if re.findall(r'(19|20)\d{2}', os.path.basename(f)) else '')) for f in glob.glob(f'{wiki}/wiki/summaries/*.md')];
      pdfs = glob.glob('/Users/lwj04/Zotero/storage/*/*.pdf');
      new_pdfs = [];
      for pdf in pdfs:
          fn = os.path.basename(pdf).lower();
          year_m = re.search(r'(19|20)\d{2}', fn);
          if not year_m: continue;
          year = year_m.group();
          author_m = re.match(r'([a-z]+)', fn);
          if not author_m: continue;
          author = author_m.group(1);
          if (author, year) in summaries: continue;
          if os.path.getsize(pdf) > 20*1024*1024: continue;
          new_pdfs.append({'pdf': pdf, 'filename': os.path.basename(pdf), 'year': year, 'size_kb': os.path.getsize(pdf)//1024});
      new_pdfs.sort(key=lambda x: x['year'], reverse=True);
      json.dump(new_pdfs[:20], open('/tmp/incremental_new.json', 'w'), ensure_ascii=False, indent=2);
      print(f'Detected {len(new_pdfs)} new PDFs, top 20 saved');
      "

  - id: convert
    description: 批量转换新检测到的 PDF
    command: >-
      BATCH_FILE=/tmp/incremental_new.json WIKI_ROOT=${WIKI_ROOT:-data/fuel_swelling_wiki}
      python3 ${WIKI_ROOT:-data/fuel_swelling_wiki}/pipeline/batch_convert.py

  - id: validate-convert
    description: 验证转换结果
    command: >-
      python3 -c "
      import json;
      data = json.load(open('/tmp/incremental_new.json'));
      print(f'Papers to ingest: {len(data)}');
      for p in data: print(f'  {p[\"filename\"][:60]} ({p[\"size_kb\"]}KB)');
      "

  - id: report
    description: 生成增量检测报告
    command: >-
      python3 -c "
      import json, os;
      data = json.load(open('/tmp/incremental_new.json'));
      wiki = os.environ.get('WIKI_ROOT', 'data/fuel_swelling_wiki');
      raw_count = len([f for f in os.listdir(f'{wiki}/raw/papers}') if f.endswith('.txt')]);
      sum_count = len([f for f in os.listdir(f'{wiki}/wiki/summaries}') if f.endswith('.md')]);
      print(f'=== Incremental Update Report ===');
      print(f'Existing: {sum_count} summaries, {raw_count} raw papers');
      print(f'New detected: {len(data)} PDFs');
      print(f'Action required: Run LLM ingest on new papers');
      print(f'Command: spawn subagent with ingest task');
      "
