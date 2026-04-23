#!/usr/bin/env python3
"""
LLM Ingest wrapper for Lobster pipeline.
Reads stdin JSON with slug/raw_path, spawns a sub-agent via OpenClaw sessions_spawn
to generate summary + parameters following llm-wiki SKILL.md.

Since this runs inside Lobster (shell), we use the openclaw CLI or direct API
to trigger sessions_spawn. Falls back to direct LLM call via llm-task if unavailable.
"""
import json, sys, os, subprocess, time

WIKI_ROOT = os.environ.get('WIKI_ROOT', os.path.expanduser('~/.openclaw/workspace/data/nuclear-materials-wiki'))
SKILL_PATH = os.environ.get('SKILL_PATH', os.path.expanduser('~/.openclaw/workspace/skills/material-llm-wiki/skills/llm-wiki/SKILL.md'))

def main():
    data = json.loads(sys.stdin.read())
    slug = data['slug']
    raw_path = data['raw_path']
    has_formulas = data.get('has_formulas', False)

    print(f"[ingest] Processing: {slug}")
    print(f"[ingest] Raw: {raw_path} ({data.get('size',0)} bytes, formulas={'yes' if has_formulas else 'no'})")

    # Read raw paper text (limit to first 80KB for LLM context)
    with open(raw_path) as f:
        paper_text = f.read(80000)

    # Read schema for parameter extraction
    schema_path = os.path.join(os.path.dirname(__file__), 'schema_parameter.json')
    with open(schema_path) as f:
        param_schema = json.load(f)

    # Read SKILL.md for ingest template
    with open(SKILL_PATH) as f:
        skill_content = f.read(30000)

    # Generate summary markdown via direct Python write
    # (The actual LLM processing should be done by sessions_spawn from the main agent)
    # For Lobster compatibility, we write a placeholder and signal completion
    summary_path = os.path.join(WIKI_ROOT, 'wiki', 'summaries', f'{slug}.md')
    params_path = os.path.join(WIKI_ROOT, 'parameters', f'{slug}.json')

    # Signal that LLM processing is needed
    result = {
        'status': 'needs_llm_spawn',
        'slug': slug,
        'raw_path': raw_path,
        'summary_path': summary_path,
        'params_path': params_path,
        'message': f'Lobster pipeline completed PDF conversion. Run: sessions_spawn(task="使用 llm-wiki skill ingest 导入论文. Raw: {raw_path}, Slug: {slug}")',
    }

    # Try to invoke llm-task directly if openclaw is available
    try:
        import urllib.request
        req = urllib.request.Request(
            'http://127.0.0.1:18789/api/tools',
            data=json.dumps({
                'tool': 'sessions_spawn',
                'action': 'run',
                'params': {
                    'task': f"""使用 llm-wiki skill 的 ingest 操作导入论文。

PDF 已转换为文本: {raw_path}
Slug: {slug}

请执行:
1. 读取 raw paper 文本
2. 生成中文摘要 → wiki/summaries/{slug}.md (200-400词,含 Key Equations)
3. 提取结构化参数 → parameters/{slug}.json (遵循 schema_parameter.json)
4. 运行 validate 检查

工作目录: {WIKI_ROOT}""",
                    'runtime': 'subagent',
                    'mode': 'run',
                    'label': f'ingest-{slug}',
                    'cleanup': 'keep',
                }
            }).encode(),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        resp = urllib.request.urlopen(req, timeout=5)
        resp_data = json.loads(resp.read())
        result['status'] = 'spawned'
        result['session_key'] = resp_data.get('childSessionKey', '')
        result['run_id'] = resp_data.get('runId', '')
        print(f"[ingest] Spawned sub-agent: {result['session_key']}")
    except Exception as e:
        print(f"[ingest] Direct spawn failed ({e}), delegating to main agent")
        result['error'] = str(e)

    print(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    main()
