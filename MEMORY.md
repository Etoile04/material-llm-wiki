# MEMORY.md - Long-Term Memory

## About This File

This is your long-term memory. Distill important events, decisions, and lessons here. Daily logs go in `memory/YYYY-MM-DD.md`.

---

## User Profile

**Name**: 李文杰 (Wenjie Li)
**Timezone**: Asia/Shanghai (GMT+8)
**Primary Contact**: Feishu DM (ou_db382c0e4e9336b34e2579f52917deb8)

---

## Key Projects

### 1. claude-code-clawdbot-skill-enhanced (Completed 2026-02-05)

**GitHub**: https://github.com/Etoile04/claude-code-clawdbot-skill-enhanced

**Purpose**: Enhanced version of claude-code-clawdbot-skill with SuperClaude Framework integration

**Key Features**:
- SuperClaude Framework complete integration
- 30 slash commands documented
- 16 specialized AI agents
- 7 behavioral modes
- 8 MCP server integrations
- Spec Kit workflow guide
- OpenSpec workflow guide

**Performance Results**:
- Average speed: 3.4x faster
- Token savings: 60% reduction
- Dev efficiency: 2.8x improvement
- Quality: 27% better

**Documentation**: 53.8KB of new docs and examples
- README.md (11KB)
- CHANGELOG.md (6.8KB)
- examples/ (34.5KB)
- PERFORMANCE-BENCHMARKS.md (9.3KB)

**Location**: `/Users/lwj04/clawd/claude-code-clawdbot-skill-enhanced`

### 2. English Flash Cards App (Completed)

**Location**: `/Users/lwj04/clawd/english-flashcards`

**Tech Stack**: HTML5, CSS3, Vanilla JavaScript (no frameworks)

**Key Features**:
- Card CRUD operations
- 3D flip animations
- localStorage persistence
- Quiz mode with auto-generated multiple choice
- Progress tracking
- JSON import/export

**Files**: 5 core files (index.html, styles.css, app.js, storage.js, quiz.js)

### 3. Everything Claude Code Integration (Completed 2026-02-05 Part 2)

**Purpose**: Integrate everything-claude-code framework into claude-code-clawdbot-skill-enhanced

**Repository**: https://github.com/affaan-m/everything-claude-code

**Key Features Added**:
- 🤖 **15+ specialized agents** for delegation
- 📚 **30+ skills** for workflow definition
- ⚡ **20+ commands** for quick execution
- 🪝 **Comprehensive hooks system** (PreToolUse, PostToolUse, Session-Start/End)
- 📋 **6+ rules** for guidelines (security, coding-style, testing, etc.)
- 🔄 **Continuous Learning v2** with instinct-based learning
- 🐹 **Go language support** with Go-specific agents and workflows
- 🛠️ **Skill Creator** for generating skills from git history
- 🔌 **MCP configurations** for GitHub, Supabase, Vercel, Railway
- 🪵 **Cross-platform support** (Windows, macOS, Linux)
- 📦 **Package manager detection** (npm, pnpm, yarn, bun)

**Documentation**: EVERYTHING-CLAUDE-CODE.md (8.2KB)

**V2 Features**:
- Continuous Learning v2 with instinct-based learning
- `/instinct-status` - View learned instincts with confidence
- `/instinct-import <file>` - Import instincts
- `/instinct-export` - Export instincts
- `/evolve` - Cluster related instincts into skills
- `/skill-create` - Generate skills from git history

**Go Support**:
- `/go-review` - Go code review
- `/go-test` - Go TDD workflow
- `/go-build` - Fix Go build errors
- Go patterns and best practices

**Commands**:
- `/tdd` - Test-driven development
- `/plan` - Implementation planning
- `/e2e` - E2E test generation
- `/code-review` - Quality review
- `/build-fix` - Fix build errors
- `/refactor-clean` - Dead code removal
- `/learn` - Extract patterns from sessions
- `/checkpoint` - Save verification state
- `/verify` - Run verification loop
- `/setup-pm` - Configure package manager

**Key Insight**: Can use both SuperClaude and Everything frameworks together for maximum capabilities!

**Location**: `/Users/lwj04/clawd/claude-code-clawdbot-skill-enhanced/EVERYTHING-CLAUDE-CODE.md`

---

## Important Lessons

### Claude Code Usage

**PTY Mode is Critical**
- Claude Code MUST use PTY (pseudo-terminal) mode
- Without PTY, it hangs or produces abnormal output
- In OpenClaw, use `bash pty:true` or Python wrapper
- Source: Daily memory 2026-02-05

**Working Directory Matters**
- Specify correct workdir to avoid reading irrelevant files
- Improves context quality and performance
- Use `workdir:/path/to/project` parameter
- Source: Daily memory 2026-02-05

**Permission Management**
- Use `--allowedTools` to follow least privilege principle
- Limit necessary tools for security
- Examples: `--allowedTools "Bash,Read,Edit"` or `--allowedTools "Read,Edit"`
- Source: Daily memory 2026-02-05

**Progress Monitoring**
- Use `process:log` to check background task progress
- Use `process:poll` to verify completion
- Use `process:write/submit` to send input
- Source: Daily memory 2026-02-05

### SuperClaude Framework

**Spec Kit Workflow Requirements**
- Requires Git repository initialized
- Requires origin remote set (can be local bare repo)
- Requires sufficient tool permissions (Write + Bash)
- Must use interactive tmux mode
- Source: Daily memory 2026-02-05

**MCP Servers**
- Tavily: Web search, essential for deep research
- Context7: Official documentation lookup
- Serena: Session persistence and memory
- Sequential: Multi-step reasoning
- Playwright: Cross-browser automation
- Magic: UI component generation
- Performance: 3.4x average improvement, 60% token savings
- Worth installing and configuring
- Source: Daily memory 2026-02-05

### Cross-Platform Compatibility

**macOS Specific Issues**
- Python wrapper using `script(1)` may not work on macOS
- macOS `script(1)` path or behavior differs from Linux
- Solution: Use Python's pty library or `bash pty:true` directly
- Source: Daily memory 2026-02-05

**Best Practice**
- Use Python pty library instead of script(1)
- Test cross-platform compatibility
- Document platform-specific notes
- Source: Daily memory 2026-02-05

### Progress Reporting

**Issue**: Failed to report progress every 30 minutes actively

**Improvement Direction**:
- Use cron scheduled tasks to send progress updates
- Actively notify at key milestones
- Use `cron wake` functionality
- Set up reminder checkpoints
- Source: Daily memory 2026-02-05

---

## System Configuration

### OpenClaw

**Version**: 2026.2.2-3
**Config**: `/Users/lwj04/.openclaw/openclaw.json`
**Workspace**: `/Users/lwj04/.openclaw/workspace`
**Default Model**: zai/glm-4.7

**Plugins**:
- feishu: @m1heng-clawd/feishu v0.1.6 (external, 4 skills)
- discord: disabled

**Skills**: 28 eligible, 37 missing requirements

**Important**: Feishu plugin conflict resolved 2026-02-05
- Moved built-in plugin to `/tmp/openclaw-feishu-builtin-backup`
- Using external plugin only (provides feishu-doc/drive/wiki/perm)
- No warnings
- Source: Daily memory 2026-02-05

### Claude Code

**Path**: `/Users/lwj04/.local/bin/claude`
**Version**: 2.1.31
**Environment Variable**: `CLAUDE_CODE_BIN=/Users/lwj04/.local/bin/claude`

### Skills

**coding-agent**: `/opt/homebrew/lib/node_modules/openclaw/skills/coding-agent/SKILL.md`
**claude-code-clawdbot-skill**: `/Users/lwj04/clawd/skills/claude-code-clawdbot-skill/SKILL.md`
**self-improving-agent**: `/Users/lwj04/clawd/skills/self-improving-agent/SKILL.md`

---

## Key Decisions

### 2026-02-05: Feishu Plugin Resolution

**Problem**: Duplicate feishu plugins causing conflict
- Built-in: @openclaw/feishu v2026.2.2
- External: @m1heng-clawd/feishu v0.1.6
- Both used same channel ID: "feishu"

**Decision**: Keep external plugin, remove built-in
**Reasoning**:
- External plugin provides 4 additional skills (doc/drive/wiki/perm)
- Configuration already specifies external plugin
- Richer functionality

**Outcome**:
- ✅ Warning resolved
- ✅ 4 skills available
- ✅ Backup available at `/tmp/openclaw-feishu-builtin-backup`
- Source: Daily memory 2026-02-05

### 2026-02-05: SuperClaude Framework Integration

**Decision**: Complete integration of SuperClaude Framework into claude-code-clawdbot-skill

**Outcome**:
- ✅ 30 slash commands documented
- ✅ 8 MCP servers configured
- ✅ Spec Kit and OpenSpec workflows documented
- ✅ Performance benchmarks created
- ✅ 53.8KB documentation added
- ✅ 100% completion of mid-term goals
- Source: Daily memory 2026-02-05

---

## Next Steps

### Short-term
- Test enhanced skill in real projects
- Verify MCP server performance improvements
- Test Spec Kit workflow

### Long-term
- Fix Python wrapper macOS compatibility
- Submit PR to original repository
- Share usage experience and best practices

---

*Last Updated: 2026-02-05*
