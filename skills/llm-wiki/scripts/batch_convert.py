#!/usr/bin/env python3
"""Batch PDF → pdftotext conversion for Lobster pipeline."""
import json, subprocess, os, sys

BATCH_FILE = os.environ.get('BATCH_FILE', '/tmp/batch2_fuel.json')
WIKI_ROOT = os.environ.get('WIKI_ROOT', os.path.expanduser('~/.openclaw/workspace/data/nuclear-materials-wiki'))

with open(BATCH_FILE) as f:
    batch = json.load(f)

out_dir = os.path.join(WIKI_ROOT, 'raw', 'papers')
os.makedirs(out_dir, exist_ok=True)

results = []
for p in batch:
    slug = p['filename'].replace('.pdf', '').replace(' ', '_')[:70]
    slug = ''.join(c if c.isalnum() or c in '_-.' else '_' for c in slug)
    out_path = os.path.join(out_dir, f'{slug}.txt')
    
    r = subprocess.run(['pdftotext', '-layout', p['pdf'], out_path], capture_output=True, text=True)
    
    if r.returncode == 0 and os.path.isfile(out_path):
        sz = os.path.getsize(out_path)
        with open(out_path) as f:
            text = f.read()
        formulas = text.count('$$')
        results.append({
            'status': 'converted',
            'slug': slug,
            'raw_path': out_path,
            'size_bytes': sz,
            'formulas': formulas,
            'needs_mineru': formulas < 6,
            'year': p.get('year', ''),
            'original_pdf': p['pdf']
        })
        print(f"  ✅ {slug[:50]} ({sz//1024}KB, formulas:{formulas})", file=sys.stderr)
    else:
        results.append({
            'status': 'error',
            'slug': slug,
            'error': r.stderr[:200] if r.stderr else 'unknown error',
            'original_pdf': p['pdf']
        })
        print(f"  ❌ {slug[:50]}: {r.stderr[:80] if r.stderr else 'failed'}", file=sys.stderr)

output = {
    'status': 'batch_converted',
    'total': len(batch),
    'converted': sum(1 for r in results if r['status'] == 'converted'),
    'errors': sum(1 for r in results if r['status'] == 'error'),
    'papers': results
}
print(json.dumps(output, ensure_ascii=False))
