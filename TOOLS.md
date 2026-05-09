# TOOLS.md

## Git Policy

**GitHub 只同步技能/代码文件，不同步数据文件。**
- `data/` 目录下的所有内容（parameters, summaries, raw PDFs, logs, archive）**禁止** `git add`
- .gitignore 已包含 `data/` 规则
- 原因：避免知识产权问题（论文摘要、提取参数、PDF 原文等）
- 违规后果：2026-04-26 曾误提交 290 个数据文件，已清理（commit `10d98f9`）

Local tool notes placeholder.

This file is intentionally minimal in the public repository.

Use it for machine-local, non-secret notes such as:

- preferred local paths
- local helper commands
- environment-specific reminders
- non-sensitive device nicknames

Do not store secrets, tokens, passwords, or personal identifiers here.

For private setups, keep detailed local notes outside the public repository or in ignored files.
