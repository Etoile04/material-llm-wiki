name: ingest-single
description: 单篇论文 PDF → pdftotext → 质量检查

steps:
  - id: convert
    command: "python3 -c \"import json,subprocess,os,sys; pdf=os.environ.get('PDF_PATH',''); slug=os.environ.get('SLUG','unknown'); wiki=os.environ.get('WIKI_ROOT',os.path.expanduser('~/.openclaw/workspace/data/nuclear-materials-wiki')); out_dir=os.path.join(wiki,'raw','papers'); os.makedirs(out_dir,exist_ok=True); out_path=os.path.join(out_dir,slug+'.txt'); r=subprocess.run(['pdftotext','-layout',pdf,out_path],capture_output=True,text=True); sz=os.path.getsize(out_path) if r.returncode==0 else 0; print(json.dumps({'status':'done' if r.returncode==0 else 'error','slug':slug,'raw_path':out_path,'size_bytes':sz,'strategy':'pdftotext'}))\""

  - id: check
    command: "python3 -c \"import json,sys,os; data=json.loads(sys.stdin.read()); path=data.get('raw_path',''); text=open(path).read() if os.path.isfile(path) else ''; dollars=text.count('$$'); lines=len(text.splitlines()); print(json.dumps({'status':'checked','slug':data['slug'],'raw_path':path,'lines':lines,'formula_indicators':dollars,'has_formulas':dollars>5,'size_bytes':data['size_bytes']}))\""
    stdin: $convert.stdout

  - id: report
    command: "python3 -c \"import json,sys; d=json.loads(sys.stdin.read()); print(json.dumps({'status':'ready_for_llm','slug':d['slug'],'lines':d['lines'],'formula_indicators':d['formula_indicators'],'formula_status':'✅' if d.get('has_formulas') else '⚠️ 需要 MinerU','next_step':'sessions_spawn llm-wiki ingest'}))\""
    stdin: $check.stdout
