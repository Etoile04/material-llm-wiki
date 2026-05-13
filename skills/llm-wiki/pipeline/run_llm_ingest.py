#!/usr/bin/env python3
"""
LLM Ingest wrapper for Lobster pipeline — v2.0

使用标准化的 prompt 生成器，输出 prompt 供调用者使用 sessions_spawn。
支持 checkpoint 持久化和断点续跑。
"""
import json, sys, os, subprocess, time

WIKI_ROOT = os.environ.get('WIKI_ROOT', '/Users/lwj04/.openclaw/workspace/data/fuel_swelling_wiki')
SKILL_PATH = '/Users/lwj04/.openclaw/workspace/skills/llm-wiki/SKILL.md'
RESUME_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lobster_resume.py')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ingest_prompt_builder import build_ingest_prompt

def main():
    data = json.loads(sys.stdin.read())
    slug = data['slug']
    raw_path = data['raw_path']
    has_formulas = data.get('has_formulas', False)
    size = data.get('size', data.get('size_bytes', 0))

    print(f"[ingest] Processing: {slug}")
    print(f"[ingest] Raw: {raw_path} ({size} bytes, formulas={'yes' if has_formulas else 'no'})")

    # Check if already completed (resume support)
    try:
        result = subprocess.run(
            ['python3', RESUME_SCRIPT, '--mode', 'status', '--slug', slug],
            capture_output=True, text=True, timeout=10
        )
        cp = json.loads(result.stdout)
        if cp.get('status') == 'done' and cp.get('step') == 'complete':
            print(f"[ingest] Already completed (resumed), skipping")
            print(json.dumps({'status': 'skipped_resumed', 'slug': slug}))
            return
    except (subprocess.TimeoutExpired, json.JSONDecodeError, KeyError):
        pass

    # Read raw paper text for context
    paper_preview = ""
    if os.path.isfile(raw_path):
        with open(raw_path) as f:
            paper_preview = f.read(40000)

    # Build standardized prompt
    prompt = build_ingest_prompt(
        slug=slug,
        raw_path=raw_path,
        wiki_root=WIKI_ROOT,
        has_formulas=has_formulas,
        file_size_bytes=size,
    )

    # Add paper preview for context
    prompt += f"\n\n## 论文预览（前 40KB）\n\n{paper_preview[:35000]}"

    # Save checkpoint before LLM processing
    subprocess.run(
        ['python3', RESUME_SCRIPT, '--mode', 'save', '--slug', slug,
         '--step', 'llm', '--status', 'in_progress',
         '--data', json.dumps({'raw_path': raw_path, 'has_formulas': has_formulas})],
        capture_output=True, timeout=10
    )

    # Output the prompt for the calling process
    result = {
        'status': 'ready_for_spawn',
        'slug': slug,
        'raw_path': raw_path,
        'summary_path': os.path.join(WIKI_ROOT, 'wiki', 'summaries', f'{slug}.md'),
        'params_path': os.path.join(WIKI_ROOT, 'parameters', f'{slug}.json'),
        'prompt': prompt,
        'prompt_size': len(prompt),
        'message': f'Prompt ready for sessions_spawn ({len(prompt)} chars)',
    }

    print(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    main()
