name: ingest-single-full
description: 完整单篇论文入库 — PDF转换 → LLM处理(Summary+Params) → Validate → Report

# 环境变量: PDF_PATH, SLUG, WIKI_ROOT

steps:
  # ── Step 1: PDF → Markdown (pdftotext) ──
  - id: convert
    command: "python3 -c \"import json,subprocess,os; pdf=os.environ.get('PDF_PATH',''); slug=os.environ.get('SLUG','unknown'); wiki=os.environ.get('WIKI_ROOT',os.path.expanduser('~/.openclaw/workspace/data/nuclear-materials-wiki')); assert pdf and os.path.isfile(pdf), f'PDF not found: {pdf}'; out_dir=os.path.join(wiki,'raw','papers'); os.makedirs(out_dir,exist_ok=True); out_path=os.path.join(out_dir,slug+'.txt'); r=subprocess.run(['pdftotext','-layout',pdf,out_path],capture_output=True,text=True); assert r.returncode==0, f'pdftotext failed: {r.stderr}'; sz=os.path.getsize(out_path); print(json.dumps({'status':'converted','slug':slug,'raw_path':out_path,'size_bytes':sz}))\""

  # ── Step 2: 质量预检 (公式覆盖率) ──
  - id: check
    command: "python3 -c \"import json,sys,os; d=json.loads(sys.stdin.read()); p=d.get('raw_path',''); t=open(p).read() if os.path.isfile(p) else ''; dol=t.count('$$'); lines=len(t.splitlines()); print(json.dumps({'status':'checked','slug':d['slug'],'raw_path':p,'lines':lines,'formulas':dol,'needs_mineru':dol<6,'size':d['size_bytes']}))\""
    stdin: $convert.stdout

  # ── Step 3: LLM 处理 (Summary + Parameters) ──
  # 由 run_llm_ingest.py 尝试直接 spawn，失败时输出委托指令
  - id: llm
    command: "python3 -c \"import os,sys; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','scripts')); import run_llm_ingest; run_llm_ingest.main()\""
    stdin: $check.stdout

  # ── Step 4: Validate ──
  - id: validate
    command: "python3 -c \"import subprocess,os; wiki=os.environ.get('WIKI_ROOT',os.path.expanduser('~/.openclaw/workspace/data/nuclear-materials-wiki')); script=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','scripts','validate_params.py'); r=subprocess.run(['python3',script,wiki],capture_output=True,text=True); [print(l) for l in r.stdout.split(chr(10)) if any(k in l for k in ['FAIL','PASS','Total','Records','Check'])][:10]; print(json.dumps({'validate':'done'}))\""

  # ── Step 5: 生成报告 ──
  - id: report
    command: "python3 -c \"import json,sys,os,glob; wiki=os.environ.get('WIKI_ROOT',os.path.expanduser('~/.openclaw/workspace/data/nuclear-materials-wiki')); sums=glob.glob(os.path.join(wiki,'wiki','summaries','*.md')); params=glob.glob(os.path.join(wiki,'parameters','*.json')); raws=glob.glob(os.path.join(wiki,'raw','papers','*')); print(json.dumps({'status':'complete','summaries':len(sums),'params_files':len(params),'raw_files':len(raws)},ensure_ascii=False))\""
    stdin: $validate.stdout
