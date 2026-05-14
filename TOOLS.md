# TOOLS.md

## Git Policy

**GitHub 只同步技能/代码文件，不同步数据文件。**
- `data/` 目录下的所有内容（parameters, summaries, raw PDFs, logs, archive）**禁止** `git add`
- .gitignore 已包含 `data/` 规则
- 原因：避免知识产权问题（论文摘要、提取参数、PDF 原文等）
- 违规后果：2026-04-26 曾误提交 290 个数据文件，已清理（commit `10d98f9`）

## NFMD Database Safety

- **子智能体规则**：任何涉及 NFMD 数据库操作的子智能体必须先加载 `nfmd-db-ops` 技能
- **禁止命令**：TRUNCATE / DROP TABLE / 无 WHERE 的 DELETE 或 UPDATE
- **事务要求**：修复脚本必须用 `BEGIN; ... COMMIT;` 包裹
- **预检步骤**：写入前先 COUNT 预览影响行数 + 确认备份存在
- **教训来源**：2026-05-11 子智能体误执行 TRUNCATE 导致全部修复回滚

Local tool notes placeholder.

This file is intentionally minimal in the public repository.

Use it for machine-local, non-secret notes such as:

- preferred local paths
- local helper commands
- environment-specific reminders
- non-sensitive device nicknames

Do not store secrets, tokens, passwords, or personal identifiers here.

For private setups, keep detailed local notes outside the public repository or in ignored files.
