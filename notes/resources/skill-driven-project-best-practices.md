# 技能驱动项目管理 — 最佳实践

> 基于 NucPot 项目（Phase 1-4 + ref-gap-fill）的实战总结

---

## 1. 项目全生命周期技能编排

### 1.1 总览：技能使用时间线

```
战略规划层    ┌── strategic-goal-tracking ──┐
              │   MSPOT + OKR               │
              └─────────────────────────────┘
                        ↕ 对齐
项目管理层    ┌── dev-project-tracker ────────────────────────────┐
              │   DASHBOARD + WORK_LOG + ISSUES + Milestones     │
              └──────────────────────────────────────────────────┘
                        ↕ 跟踪
设计决策层    ┌── brainstorming → writing-plans → specs ──┐
              │   逐个澄清 → 方案冻结 → 正式规格         │
              └────────────────────────────────────────────┘
                        ↕ 指导
开发执行层    ┌── subagent-driven-development ──┐
              │   task → spawn → yield → verify │
              └──────────────────────────────────┘
                        ↕ 交付
质量保障层    ┌── verification → code-review → finishing-branch ──┐
              │   测试 → 审查 → 合并                               │
              └────────────────────────────────────────────────────┘
                        ↕ 积累
知识管理层    ┌── PARA + MEMORY.md + memory/YYYY-MM-DD.md ──┐
              │   项目归档 / 资源沉淀 / 经验蒸馏              │
              └───────────────────────────────────────────────┘
```

### 1.2 每个阶段该用什么技能

| 阶段 | 首选技能 | 辅助技能 | 产出物 |
|------|----------|----------|--------|
| **战略规划** | strategic-goal-tracking | — | MSPOT 策略 + OKR 季度目标 |
| **需求分析** | brainstorming | dev-project-tracker (建目录) | 设计决策清单 + 项目 README |
| **方案设计** | writing-plans | darwin-skill (基线评估) | spec 文档 + 实施计划 |
| **代码开发** | subagent-driven-development | using-git-worktrees | 功能代码 + 测试 |
| **质量验证** | verification-before-completion | test-driven-development | 测试报告 + lint 结果 |
| **代码审查** | requesting-code-review → receiving-code-review | — | 审查意见 + 修复 |
| **合并发布** | finishing-a-development-branch | — | PR + changelog |
| **运维监控** | nfmd-db-ops | — | 数据库变更脚本 |
| **知识沉淀** | para-second-brain | dev-project-tracker (归档) | PARA 整理 + MEMORY 更新 |

---

## 2. 六条核心实践

### 实践 1：brainstorming 是设计阶段的硬门控

**原则：** 不跳过 brainstorming，不在用户批准前写代码。

**流程：**
1. 逐个提出开放问题（一次一个，不合并）
2. 每个问题给出 A/B/C 选项 + 推荐理由
3. 用户选择后记录决策
4. 所有问题澄清后，写完整设计
5. 用户批准后才进入 writing-plans

**反例（教训）：** ref-gap-fill 初版直接写 monolithic pipeline，后来发现架构不合理，被迫重新 brainstorming。浪费了 ~2 小时。

**适用场景：** 任何涉及架构选择、多方案比较、影响超过 3 天工作量的设计。

---

### 实践 2：subagent-driven-development 替代手写脚本

**原则：** 复杂工作用 subagent 拆分，不用 bash 脚本串联。

**流程：**
1. 写计划（writing-plans）拆分为独立 task
2. 每个 task 用 `sessions_spawn` 派发子 agent
3. 主 agent 用 `sessions_yield` 等待完成
4. 验证结果（verification-before-completion）

**优势：**
- 每个 subagent 有独立 context，不互相污染
- 失败的 task 可以单独重试
- 并行无依赖的 task（B/C 同时启动）

**适用场景：** 3 个以上独立子任务、需要并行、涉及不同工具栈。

---

### 实践 3：dev-project-tracker 贯穿始终

**原则：** 项目创建第一天就建目录，每次进展都更新 WORK_LOG。

**目录结构：**
```
projects/<project>/
├── README.md        # 状态 + 里程碑 + 技术栈
├── WORK_LOG.md      # 按日期的进展日志
├── ISSUES.md        # 活跃问题追踪
└── CHANGES.md       # 变更记录
```

**关键时机：**
- **启动时**：建 README + WORK_LOG，设里程碑
- **每日**：更新 WORK_LOG，同步 memory/YYYY-MM-DD.md
- **遇到问题时**：立即写入 ISSUES.md
- **方案变更时**：写入 CHANGES.md
- **里程碑完成时**：更新 README 状态 + DASHBOARD

**反例（教训）：** NucPot Phase 1-2 没有建 tracker，导致后来回忆 Phase 1 的决策需要翻 session history。

---

### 实践 4：PARA 整理是项目收尾的必要步骤

**原则：** 设计文档、可复用资产、经验教训分别归入 PARA 的 Projects / Resources / Archive。

**映射规则：**
| 内容类型 | PARA 归类 | 路径 |
|----------|----------|------|
| 活跃项目 + 设计文档 | Projects | `notes/projects/<name>/` |
| 可复用资产审计 | Resources | `notes/resources/<name>-audit.md` |
| 经验教训 | Resources / MEMORY.md | `notes/resources/<topic>.md` |
| 已完成项目 | Archive | `notes/archive/<name>/` |

**关键操作：**
- 源文件保持 canonical 位置，notes/ 中用 symlink 指向
- `memory/notes → ../notes` symlink 保证 memory_search 可索引
- 每次项目阶段结束时做 PARA 整理

---

### 实践 5：可复用资产审计降低开发成本

**原则：** 动手写代码前，先做资产盘点。

**清单：**
1. **直接复用**：哪些脚本/API/数据可以直接调用？
2. **需要适配**：哪些功能已有但接口不同？
3. **必须新建**：哪些能力完全缺失？

**效果量化（ref-gap-fill 案例）：**
- 直接复用 9 项（ontofuel API、llm-wiki pipeline、zotero_sync 等）
- 需适配 3 项（中文参数映射、本体扩展、prompt 增强）
- 必须新建 7 项（property-mapping、cache-query、agents 等）
- **节省约 40% 工期**（10-15 天 → 6-10 天）

**适用场景：** 任何涉及已有系统集成的项目，尤其是 Phase 3+ 的功能扩展。

---

### 实践 6：strategic-goal-tracking 保证项目不偏航

**原则：** OKR 与 MSPOT 对齐，每周 review 防止 scope creep。

**三层联动：**
```
MSPOT (战略) → OKR (季度目标) → PARA (日常执行)
     ↓               ↓                ↓
  方向+边界      可量化进度        文件+任务
```

**实际使用模式：**
- OKR 的 KR 对应 projects/ 下的子项目
- 每个 KR 有 tracker 目录 (kr1_xxx/, kr2_xxx/)
- MSPOT 的 Omissions 清单防止 scope creep
- DASHBOARD.md 是全局视图

---

## 3. 技能使用流水线（Pipeline）

### 3.1 新项目启动流程

```
1. strategic-goal-tracking
   → 创建/确认 MSPOT + OKR
   → 在 DASHBOARD.md 中添加项目

2. dev-project-tracker
   → 创建 projects/<name>/ 目录
   → README.md + WORK_LOG.md + ISSUES.md

3. brainstorming
   → 逐个澄清设计决策
   → 记录到 Decisions 表

4. writing-plans
   → 写 spec 到 docs/superpowers/specs/
   → 写 plan 到 docs/superpowers/plans/

5. 可复用资产审计
   → 盘点现有技能/脚本/数据
   → 输出复用/适配/新建清单

6. subagent-driven-development
   → 按 plan 拆分 task
   → 逐个 spawn subagent
   → yield + verify

7. verification-before-completion
   → 测试 + lint + 构建
   → 确认所有 gate 通过

8. finishing-a-development-branch
   → PR + changelog
   → 合并到 main

9. PARA 整理
   → notes/projects/ 项目页
   → notes/resources/ 资源页
   → MEMORY.md 经验蒸馏

10. dev-project-tracker 更新
    → WORK_LOG 记录完成
    → README 状态更新
    → DASHBOARD 刷新
```

### 3.2 技能选择决策树

```
需要做决策？
  → brainstorming

需要写计划？
  → writing-plans

需要写代码？
  → subagent-driven-development
    ↳ 代码质量？→ test-driven-development
    ↳ 调试？→ systematic-debugging
    ↳ worktree？→ using-git-worktrees

需要验证？
  → verification-before-completion

需要审查？
  → requesting-code-review → receiving-code-review

需要合并？
  → finishing-a-development-branch

需要跟踪？
  → dev-project-tracker + DASHBOARD

需要归档？
  → para-second-brain

需要战略对齐？
  → strategic-goal-tracking
```

---

## 4. 常见反模式

| 反模式 | 后果 | 正确做法 |
|--------|------|----------|
| 跳过 brainstorming 直接写代码 | 方向错误，大范围返工 | 先澄清所有开放问题 |
| 一个技能包打天下 | monolithic pipeline 难维护 | 按职责拆分多智能体 |
| 不做资产审计就新建 | 重复造轮子，工期膨胀 | 先盘点再开发 |
| 项目文档和代码分离 | 文档过时，失去参考价值 | tracker 目录和代码同仓库 |
| DASHBOARD 不更新 | 全局视图失效，优先级混乱 | 每次里程碑后刷新 |
| memory/notes 不做 symlink | search 找不到项目笔记 | 建好 symlink 保证可搜索 |
| WORK_LOG 混入个人日志 | 项目信息淹没在噪声中 | 项目进展写 WORK_LOG，个人日志写 memory/ |
| OKR 和 tracker 脱钩 | 不知道 KR 进度 | 每个 KR 对应 tracker 子目录 |

---

## 5. 技能成熟度评估

基于 NucPot 项目实战，对使用过的技能评级：

| 技能 | 使用频率 | 效果 | 成熟度 | 备注 |
|------|----------|------|--------|------|
| brainstorming | 高 | 优秀 | ⭐⭐⭐⭐⭐ | 逐个提问是关键 |
| writing-plans | 高 | 优秀 | ⭐⭐⭐⭐⭐ | spec + plan 双文件清晰 |
| subagent-driven-dev | 高 | 优秀 | ⭐⭐⭐⭐ | 并行效果好，但需注意 task 边界 |
| dev-project-tracker | 高 | 良好 | ⭐⭐⭐⭐ | 结构清晰，需坚持更新 |
| para-second-brain | 中 | 良好 | ⭐⭐⭐⭐ | symlink 技巧是关键 |
| strategic-goal-tracking | 低 | 良好 | ⭐⭐⭐ | MSPOT 过重，OKR 实用 |
| darwin-skill | 低 | 一般 | ⭐⭐⭐ | 9 维 rubric 有价值，但流程长 |
| verification-before-completion | 中 | 优秀 | ⭐⭐⭐⭐⭐ | gate 检查防止低质量交付 |
| nfmd-db-ops | 高 | 必需 | ⭐⭐⭐⭐⭐ | 安全规则避免数据灾难 |
| Lobster | 低 | 一般 | ⭐⭐⭐ | 适合确定性流程，不适合灵活编排 |

---

## 6. 总结：五条原则

1. **先想后做** — brainstorming 是设计门控，不跳过
2. **先查后建** — 资产审计在编码前，避免重复
3. **边做边记** — tracker 贯穿始终，DASHBOARD 实时更新
4. **做完整理** — PARA 归档 + MEMORY 蒸馏是收尾标配
5. **技能组合** — 没有单一技能能完成复杂项目，pipeline > monolith
