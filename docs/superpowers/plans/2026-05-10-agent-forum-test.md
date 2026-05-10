# Agent Forum Skill — Test & Improvement Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** End-to-end test and iteratively improve the agent-forum skill through a structured multi-round forum run, fixing issues found during execution.

**Architecture:** The agent-forum skill uses OpenClaw's `sessions_spawn` (parallel subagents with different models) + `llm-task` (structured moderator output) + JSON state persistence. We test by running a real forum on a real topic, validate each step's output, and fix issues inline.

**Tech Stack:** OpenClaw skills system, `sessions_spawn`, `llm-task`, JSON state files, Markdown reports

---

## Context for Subagents

### Skill Location
- Main skill: `~/.openclaw/skills/agent-forum/SKILL.md`
- Templates: `~/.openclaw/skills/agent-forum/references/templates.md`
- Examples: `~/.openclaw/skills/agent-forum/references/examples.md`
- Base debate skill: `~/.openclaw/workspace/skills/multi-agent-debate/SKILL.md`

### State & Output Location
- State file: `~/.openclaw/workspace/agent-forum/<topic-slug>/state.json`
- Round files: `~/.openclaw/workspace/agent-forum/<topic-slug>/rounds/round-N.md`
- Report: `~/.openclaw/workspace/agent-forum/<topic-slug>/report.md`

### Forum Test Configuration
- **Topic**: U-Zr 燃料辐照肿胀与裂变气体释放的多尺度耦合机制
- **Participants**: 3 agents (sonnet, glm5.1, gpt5.4)
- **Max rounds**: 3 (controlled test, expand later)
- **Language**: zh-CN
- **Moderator model**: glm5.1

---

## Task 1: Verify Skill Loading & Configuration

**Files:**
- Verify: `~/.openclaw/skills/agent-forum/SKILL.md`
- Verify: `~/.openclaw/skills/agent-forum/references/templates.md`
- Verify: `~/.openclaw/skills/agent-forum/references/examples.md`
- Create: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/state.json`

- [ ] **Step 1: Verify skill files exist and are well-formed**

```bash
ls -la ~/.openclaw/skills/agent-forum/SKILL.md
ls -la ~/.openclaw/skills/agent-forum/references/templates.md
ls -la ~/.openclaw/skills/agent-forum/references/examples.md
```

Expected: All 3 files exist, SKILL.md > 10KB

- [ ] **Step 2: Check SKILL.md frontmatter has correct trigger words**

Run: `head -5 ~/.openclaw/skills/agent-forum/SKILL.md`
Expected: `name: agent-forum` and description mentions "multi-agent forum"

- [ ] **Step 3: Verify multi-agent-debate skill is installed**

```bash
ls -la ~/.openclaw/workspace/skills/multi-agent-debate/SKILL.md
```

Expected: File exists

- [ ] **Step 4: Create output directory**

```bash
mkdir -p ~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/rounds
```

Expected: Directory created

- [ ] **Step 5: Verify required tools are available**

Confirm these tools can be called: `sessions_spawn`, `llm-task`, `write`, `read`
Expected: All available (they are core OpenClaw tools)

- [ ] **Step 6: Commit verification**

```bash
cd ~/.openclaw/workspace
git add -A
git commit -m "test(agent-forum): verify skill files and prepare test directory"
```

---

## Task 2: Initialize Forum State

**Files:**
- Create: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/state.json`

- [ ] **Step 1: Create initial state JSON**

Write the file `agent-forum/u-zr-swelling-fgr-coupling/state.json` with:
```json
{
  "topic": "U-Zr 燃料辐照肿胀与裂变气体释放的多尺度耦合机制",
  "config": {
    "maxRounds": 3,
    "participants": [
      {
        "id": "expert-a",
        "model": "sonnet",
        "persona": "材料科学理论专家，专注于辐照损伤的原子尺度机制和热力学原理",
        "focus": "点缺陷演化、气泡形核与长大、空洞肿胀的物理机制"
      },
      {
        "id": "expert-b",
        "model": "glm5.1",
        "persona": "实验研究专家，具有丰富的辐照测试和表征经验",
        "focus": "经验数据、测量技术、组织表征、肿胀曲线与FGR数据的解读"
      },
      {
        "id": "expert-c",
        "model": "gpt5.4",
        "persona": "工程应用与数值模拟专家",
        "focus": "BISON/FEAST建模、工程安全裕度、性能预测、多尺度耦合方法"
      }
    ],
    "moderatorModel": "glm5.1",
    "convergenceThreshold": 0.8,
    "questionsPerRound": 5,
    "language": "zh-CN"
  },
  "status": "initialized",
  "currentRound": 0,
  "candidateQuestions": [],
  "mindMap": {
    "root": {
      "concept": "U-Zr 燃料辐照肿胀与FGR多尺度耦合",
      "covered": false,
      "children": [
        { "concept": "辐照肿胀机制", "covered": false, "children": [] },
        { "concept": "裂变气体释放机制", "covered": false, "children": [] },
        { "concept": "多尺度耦合方法", "covered": false, "children": [] },
        { "concept": "实验表征数据", "covered": false, "children": [] },
        { "concept": "工程预测模型", "covered": false, "children": [] },
        { "concept": "合金成分效应", "covered": false, "children": [] },
        { "concept": "温度与燃耗依赖性", "covered": false, "children": [] }
      ]
    }
  },
  "rounds": [],
  "report": null
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('agent-forum/u-zr-swelling-fgr-coupling/state.json')); print('Valid JSON')"
```

Expected: `Valid JSON`

- [ ] **Step 3: Commit**

```bash
git add agent-forum/u-zr-swelling-fgr-coupling/state.json
git commit -m "test(agent-forum): initialize forum state for U-Zr test"
```

---

## Task 3: Execute Round 1 — Question Generation & Voting

**Files:**
- Modify: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/state.json`

This task tests the moderator's ability to generate questions and select the best one.

- [ ] **Step 1: Generate candidate questions via llm-task**

Call `llm-task` with:
- model: `glm5.1`
- prompt: moderator-generate-questions template from `references/templates.md`
- input: topic, mindMap, empty pastQuestions, empty candidatePool
- schema: array of question objects (see templates.md)
- thinking: medium

Expected: Returns 5 candidate questions in valid JSON, each with id, text, targetedConcepts, rationale, difficulty

- [ ] **Step 2: Validate question quality**

Check each question:
- Is it specific enough to generate substantive discussion? (not "tell me about X")
- Does it target mind map concepts?
- Is at least one "unknown unknown" type?
- Are they in zh-CN?

If quality issues found, note them for SKILL.md improvement.

- [ ] **Step 3: Score and select question via llm-task**

Call `llm-task` with:
- model: `glm5.1`
- prompt: moderator-score-questions template
- input: candidate questions, mindMap gaps
- schema: rankings + selected question

Expected: Returns ranked list with scores, top question selected

- [ ] **Step 4: Update state.json**

Add candidate questions to pool, set selectedQuestion, update status to "round-1-in-progress", increment currentRound to 1

- [ ] **Step 5: Commit**

```bash
git add agent-forum/u-zr-swelling-fgr-coupling/state.json
git commit -m "test(agent-forum): round 1 question generated and selected"
```

---

## Task 4: Execute Round 1 — Parallel Independent Answers

**Files:**
- Modify: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/state.json`

This task tests the core parallel spawn mechanism — 3 participants answering independently with different models.

- [ ] **Step 1: Spawn Expert A (sonnet) — independent answer**

Call `sessions_spawn`:
- model: `sonnet`
- mode: `run`
- task: participant-answer template, with expert-a's persona and focus
- context: isolated (no context leakage)

- [ ] **Step 2: Spawn Expert B (glm5.1) — independent answer**

Call `sessions_spawn`:
- model: `glm5.1`
- mode: `run`
- task: participant-answer template, with expert-b's persona and focus
- context: isolated

- [ ] **Step 3: Spawn Expert C (gpt5.4) — independent answer**

Call `sessions_spawn`:
- model: `gpt5.4`
- mode: `run`
- task: participant-answer template, with expert-c's persona and focus
- context: isolated

**IMPORTANT**: Steps 1-3 should be dispatched in parallel (all three sessions_spawn calls together, then wait for results).

- [ ] **Step 4: Validate answers**

For each answer, check:
- 300-600 words? (reasonable length)
- Draws on their specific expertise?
- Notes caveats/limitations?
- In zh-CN?
- Contains specific evidence or reasoning (not generic)?

- [ ] **Step 5: Update state.json with answers**

Save all 3 answers to `rounds[0].answers`

- [ ] **Step 6: Commit**

```bash
git add agent-forum/u-zr-swelling-fgr-coupling/state.json
git commit -m "test(agent-forum): round 1 independent answers collected"
```

---

## Task 5: Execute Round 1 — Cross-Examination

**Files:**
- Modify: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/state.json`

This task tests the structured critique mechanism — each participant reviews others' work.

- [ ] **Step 1: Spawn Expert A — cross-examination**

Call `sessions_spawn`:
- model: `sonnet`
- task: participant-challenge template, with own answer + other 2 answers (anonymized)

- [ ] **Step 2: Spawn Expert B — cross-examination**

Call `sessions_spawn`:
- model: `glm5.1`
- task: participant-challenge template

- [ ] **Step 3: Spawn Expert C — cross-examination**

Call `sessions_spawn`:
- model: `gpt5.4`
- task: participant-challenge template

**IMPORTANT**: Steps 1-3 in parallel.

- [ ] **Step 4: Validate cross-examinations**

For each challenge, check:
- Uses ✓/⚠️/✗/❓ format from multi-agent-debate?
- Identifies genuine strengths and weaknesses?
- Self-reflection section present?
- Constructive, not just dismissive?

- [ ] **Step 5: Update state.json with challenges**

- [ ] **Step 6: Commit**

```bash
git add agent-forum/u-zr-swelling-fgr-coupling/state.json
git commit -m "test(agent-forum): round 1 cross-examination completed"
```

---

## Task 6: Execute Round 1 — Synthesis & Round File

**Files:**
- Modify: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/state.json`
- Create: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/rounds/round-1.md`

- [ ] **Step 1: Moderator synthesis via llm-task**

Call `llm-task`:
- model: `glm5.1`
- prompt: moderator-synthesize template
- input: all answers + all challenges + current mind map
- schema: summary, consensusPoints, debatePoints, newQuestions, coverageDelta, mindMapUpdate

- [ ] **Step 2: Validate synthesis**

Check:
- Consensus points accurate (reflect actual agreement)?
- Debate points fairly represent both sides?
- New questions are non-trivial?
- Coverage delta maps to mind map concepts?

- [ ] **Step 3: Update mind map**

Apply mindMapUpdate from synthesis to the state's mindMap. Mark covered concepts.

- [ ] **Step 4: Add new questions to candidate pool**

- [ ] **Step 5: Write round-1.md**

Compile the full round into a readable markdown file.

- [ ] **Step 6: Update state.json**

Set round synthesis, update status.

- [ ] **Step 7: Commit**

```bash
git add agent-forum/u-zr-swelling-fgr-coupling/
git commit -m "test(agent-forum): round 1 synthesis complete, mind map updated"
```

---

## Task 7: Execute Rounds 2 & 3 (Condensed)

**Files:**
- Modify: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/state.json`
- Create: `rounds/round-2.md`, `rounds/round-3.md`

Repeat Tasks 3-6 for rounds 2 and 3. Each round follows:
1. Generate questions (from updated pool + gaps)
2. Vote & select
3. Parallel independent answers
4. Parallel cross-examination
5. Synthesis + mind map update + round file

After round 3, check convergence. If coverage >= 80% or maxRounds reached, proceed to report.

- [ ] **Step 1: Execute Round 2** (steps 3-6 from above, as one subagent task)
- [ ] **Step 2: Execute Round 3** (steps 3-6 from above, as one subagent task)
- [ ] **Step 3: Check convergence**
- [ ] **Step 4: Commit after each round**

---

## Task 8: Generate Final Report

**Files:**
- Create: `~/.openclaw/workspace/agent-forum/u-zr-swelling-fgr-coupling/report.md`
- Modify: `state.json` (status → completed, add report path)

- [ ] **Step 1: Compile report via llm-task**

Call `llm-task`:
- model: `glm5.1`
- prompt: compile-report template from references/templates.md
- input: all round syntheses, final mind map, participant list
- thinking: medium

- [ ] **Step 2: Validate report quality**

Check:
- All sections present (摘要, 背景, 逐轮发现, 共识, 争议, 知识盲区)?
- Consensus points match what was actually agreed?
- Open questions are genuine (not trivial)?
- Methodology section documents models used?
- In zh-CN?

- [ ] **Step 3: Save report.md**

- [ ] **Step 4: Update state.json** — status: "completed"

- [ ] **Step 5: Commit**

```bash
git add agent-forum/u-zr-swelling-fgr-coupling/
git commit -m "test(agent-forum): final report generated, forum complete"
```

---

## Task 9: Review & Improve SKILL.md

**Files:**
- Modify: `~/.openclaw/skills/agent-forum/SKILL.md`
- Modify: `~/.openclaw/skills/agent-forum/references/templates.md`

Based on issues found during Tasks 3-8, improve the skill.

- [ ] **Step 1: Collect all issues found during execution**

Review test results and list:
- Prompt issues (unclear, missing context, wrong format)
- State management issues (missing fields, race conditions)
- Spawn issues (model unavailable, timeout, format mismatch)
- Quality issues (shallow answers, missing critique format)

- [ ] **Step 2: Fix SKILL.md**

Apply fixes:
- Clarify ambiguous instructions
- Add missing error handling
- Improve prompt templates if outputs were low quality
- Add convergence tuning tips

- [ ] **Step 3: Fix templates.md**

Update prompt templates based on what worked and what didn't.

- [ ] **Step 4: Verify changes**

Re-read updated SKILL.md end-to-end, check consistency.

- [ ] **Step 5: Commit**

```bash
cd ~/.openclaw
git add skills/agent-forum/
git commit -m "improve(agent-forum): refine skill based on end-to-end test results"
```

---

## Task 10: Final Verification & Summary

**Files:**
- All files in `agent-forum/` directory

- [ ] **Step 1: Verify state.json is valid and complete**

```bash
python3 -c "
import json
s = json.load(open('agent-forum/u-zr-swelling-fgr-coupling/state.json'))
assert s['status'] == 'completed'
assert len(s['rounds']) == 3
assert s['report'] is not None or 'report.md' in str(s)
print('State valid: %d rounds, status=%s' % (len(s['rounds']), s['status']))
"
```

- [ ] **Step 2: Verify report.md exists and is substantive**

```bash
wc -l agent-forum/u-zr-swelling-fgr-coupling/report.md
```

Expected: > 100 lines

- [ ] **Step 3: Verify round files exist**

```bash
ls -la agent-forum/u-zr-swelling-fgr-coupling/rounds/
```

Expected: round-1.md, round-2.md, round-3.md

- [ ] **Step 4: Generate test summary report**

Write a brief summary of:
- What worked well
- What needed fixing
- Skill improvements applied
- Recommendations for future iterations

- [ ] **Step 5: Final commit**

```bash
git add agent-forum/
git commit -m "test(agent-forum): end-to-end test complete with summary"
```
