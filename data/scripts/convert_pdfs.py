#!/usr/bin/env python3
"""
PDF to Markdown batch converter for fuel swelling wiki.
Uses PyMuPDF (fitz) for text extraction with structure preservation.
Falls back to pdftotext if PyMuPDF fails.

Usage: python3 convert_pdfs.py <batch.json> <output_dir>
"""
import json, os, sys, re, subprocess, shutil

def pdf_to_markdown_pymupdf(pdf_path: str) -> str:
    """Extract PDF content to structured Markdown using PyMuPDF."""
    import fitz
    
    doc = fitz.open(pdf_path)
    sections = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        
        if not text.strip():
            continue
        
        # Clean up text
        lines = text.split('\n')
        cleaned = []
        for line in lines:
            line = line.strip()
            if not line:
                if cleaned and cleaned[-1] != '':
                    cleaned.append('')
                continue
            # Detect potential headers (short lines, often bold/larger font)
            if len(line) < 80 and not line.endswith('.') and not line.startswith('•') and not line.startswith('-'):
                # Could be a section header
                if re.match(r'^[A-Z0-9]', line) and not any(c in line for c in ':;=<>'):
                    cleaned.append(f'### {line}')
                    continue
            cleaned.append(line)
        
        if cleaned:
            sections.append(f'## Page {page_num + 1}\n\n' + '\n'.join(cleaned))
    
    doc.close()
    
    if not sections:
        return ""
    
    # Get PDF metadata
    doc = fitz.open(pdf_path)
    meta = doc.metadata
    doc.close()
    
    header = f"# {meta.get('title', os.path.basename(pdf_path))}\n\n"
    if meta.get('author'):
        header += f"**Author**: {meta['author']}\n"
    if meta.get('subject'):
        header += f"**Subject**: {meta['subject']}\n"
    header += f"**Pages**: {len(doc)}\n\n---\n\n"
    
    return header + '\n\n'.join(sections)


def pdf_to_markdown_pdftotext(pdf_path: str) -> str:
    """Fallback: use pdftotext CLI."""
    import subprocess
    r = subprocess.run(
        ['pdftotext', '-layout', pdf_path, '-'],
        capture_output=True, text=True, timeout=60
    )
    if r.returncode != 0:
        return ""
    
    meta_header = f"# {os.path.basename(pdf_path)}\n\n---\n\n"
    return meta_header + r.stdout


def slugify(title: str) -> str:
    s = title[:60]
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s]+', '_', s).strip('_')
    return s


def process_batch(batch_json: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    
    # MinerU CLI path
    mineru_bin = os.path.expanduser('~/.venvs/mineru/bin/mineru')
    mineru_available = os.path.exists(mineru_bin)
    
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
        
        print(f"[{i}/{total}] {title[:60]}")
        
        if not pdf_path or not os.path.exists(pdf_path):
            print(f"  ❌ PDF not found")
            fail += 1
            continue
        
        out_file = os.path.join(output_dir, f"{slug}.md")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 100:
            print(f"  ⏭️  Already exists ({os.path.getsize(out_file)} bytes)")
            skip += 1
            continue
        
        md_content = ""
        method = ""
        
        # Method 1: MinerU CLI (best quality)
        if mineru_available:
            try:
                tmp_out = f'/tmp/mineru_{slug}'
                os.makedirs(tmp_out, exist_ok=True)
                r = subprocess.run(
                    [mineru_bin, '-p', pdf_path, '-o', tmp_out, '-b', 'pipeline', '-m', 'auto'],
                    capture_output=True, text=True, timeout=300
                )
                if r.returncode == 0:
                    # Find the output markdown
                    for root, dirs, files in os.walk(tmp_out):
                        for f in files:
                            if f.endswith('.md'):
                                fp = os.path.join(root, f)
                                with open(fp, encoding='utf-8') as fh:
                                    md_content = fh.read()
                                break
                        if md_content:
                            break
                    # Cleanup temp
                    shutil.rmtree(tmp_out, ignore_errors=True)
                    method = "MinerU"
            except Exception as e:
                print(f"  MinerU failed: {e}, trying fallback...")
        
        # Method 2: pdftotext (fallback)
        if not md_content:
            try:
                md_content = pdf_to_markdown_pdftotext(pdf_path)
                method = "pdftotext"
            except Exception as e:
                print(f"  ❌ All methods failed: {e}")
                fail += 1
                continue
        
        if md_content and len(md_content) > 100:
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
            print(f"  ✅ {method}: {os.path.getsize(out_file)} bytes")
            success += 1
        else:
            print(f"  ❌ Empty or too short output")
            fail += 1
    
    print(f"\n{'='*40}")
    print(f"Total: {total} | ✅ {success} | ⏭️ {skip} | ❌ {fail}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <batch.json> <output_dir>")
        sys.exit(1)
    process_batch(sys.argv[1], sys.argv[2])
