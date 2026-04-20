#!/usr/bin/env python3
"""Batch MinerU processing: convert PDFs to Markdown for fuel swelling wiki."""
import json, os, sys, subprocess, re

def slugify(title: str) -> str:
    s = title[:50]
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s]+', '_', s).strip('_')
    return s

def process_batch(batch_json: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(batch_json, encoding='utf-8') as f:
        items = json.load(f)
    
    total = len(items)
    success = 0
    skip = 0
    fail = 0
    
    for i, item in enumerate(items, 1):
        pdf_path = item.get('pdf_path', '')
        title = item.get('title', f'paper_{i}')
        slug = slugify(title)
        
        print(f"\n[{i}/{total}] {title[:60]}")
        
        if not pdf_path or not os.path.exists(pdf_path):
            print(f"  ❌ PDF not found: {pdf_path[:60]}")
            fail += 1
            continue
        
        # Check if already processed
        out_file = os.path.join(output_dir, f"{slug}.md")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 100:
            print(f"  ⏭️  Already exists ({os.path.getsize(out_file)} bytes)")
            skip += 1
            continue
        
        print(f"  🔄 Processing with MinerU...")
        try:
            result = subprocess.run(
                ['uvx', '--from', 'mcp-mineru', '--python', '3.12',
                 'python', '/Users/lwj04/.openclaw/skills/mineru-pdf/parse.py',
                 pdf_path, output_dir, '--backend', 'pipeline'],
                capture_output=True, text=True, timeout=300
            )
            if result.returncode == 0:
                # Find the output file
                for f in os.listdir(output_dir):
                    if f.endswith('.md') and slug[:15].lower() in f.lower():
                        success += 1
                        sz = os.path.getsize(os.path.join(output_dir, f))
                        print(f"  ✅ Created: {f} ({sz} bytes)")
                        break
                else:
                    # MinerU might name it differently, check for any new .md
                    print(f"  ✅ MinerU completed (check output dir)")
                    success += 1
            else:
                print(f"  ❌ Failed: {result.stderr[:100]}")
                fail += 1
        except subprocess.TimeoutExpired:
            print(f"  ❌ Timeout (>300s)")
            fail += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")
            fail += 1
    
    print(f"\n{'='*40}")
    print(f"Total: {total} | ✅ {success} | ⏭️ {skip} | ❌ {fail}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <batch.json> <output_dir>")
        sys.exit(1)
    process_batch(sys.argv[1], sys.argv[2])
