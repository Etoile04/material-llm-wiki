# NucPot 验证工作流开发 — 全面总结

> 时间跨度: 2026-05-25 ~ 2026-05-30 (6 天)
> 作者: agent-main | 审阅: 李文杰

---

## 一、项目全景

### 1.1 NucPot 是什么

NucPot（核材料原子间势函数开放平台）是一个面向核材料研究人员的在线平台，核心功能是**自动化验证分子动力学势函数的质量**。

### 1.2 完整架构

```
用户浏览器
  ├─ https://nucpot.dpdns.org → Cloudflare CDN → Vercel (Next.js 前端)
  │     ├─ 势函数浏览/搜索/对比
  │     ├─ 管理后台 (上传/验证)
  │     └─ 验证结果展示
  │
  ├─ https://verify.nucpot.dpdns.org → Cloudflare Named Tunnel → ThinkStation:8001
  │     ├─ FastAPI 验证服务 (nucpot-autovc)
  │     ├─ LAMMPS 计算后端 (5 种物理属性)
  │     └─ 参考值 CRUD API
  │
  ├─ ThinkStation:5432 (nucpot-db)
  │     ├─ reference_values (23条, UNIQUE约束)
  │     ├─ potentials
  │     └─ verifications
  │
  ├─ ThinkStation:15432 (nfmd-postgres)
  │     ├─ parameters (43条)
  │     ├─ materials
  │     └─ literature
  │
  └─ 多智能体系统 (OpenClaw)
        ├─ nucpot-db: 三级缓存 + 编排
        ├─ nucpot-librarian: 快线搜索提取
        └─ researcher: 审查确认
```

### 1.3 技术栈

| 层 | 技术 | 说明 |
|---|------|------|
| 前端 | Next.js 15 + Tailwind CSS | 12 页面, 18 API 端点 |
| 后端验证 | Python FastAPI + LAMMPS | 4 验证模板, 5 计算属性 |
| 数据库 | PostgreSQL (nucpot) + PostgreSQL (nfmd) | Docker 容器 |
| 部署 | Vercel + Cloudflare Tunnel | 全球 CDN |
| 自动化 | OpenClaw + ref-gap-fill | 多智能体参考值补全 |

---

## 二、开发时间线

### Day 1 (05-25 周日): 知识库提取 + 文献同步

**内容**: OntoFuel 本体驱动提取 6 篇新增 UMo 文献
- 发现 Zotero 新增 7 篇 PDF（排除 Park 2023 HTML 快照）
- 设计 OntoFuel + Lobster 4-phase 工作流
- 注册 cron job 凌晨 1:00 自动触发
- 产出: pipeline/ontofuel_umo_batch.lobster + ontofuel_umo_task.md

**意义**: 建立了文献→知识库的自动化管道

### Day 2 (05-26 周一): NucPot 网站评审

**内容**: 全面测试 nucpot.dpdns.org
- 注册/登录/角色隔离验证通过
- 发现 14 条改进建议（6 使用者 + 4 开发者 + 4 工程通用）
- 高优先级: 分页 UI、元素筛选器、温度过滤、对比功能

**意义**: 从用户视角识别了平台的可用性差距

### Day 3 (05-27 周二): 验证管线 + 云部署 (马拉松日, 16h)

这是最关键的一天，完成了从验证管线到公网部署的全栈工作。

**阶段 1 (05:00-08:00): 验证管线 Phase 2**
- nucpot-autovc 参数化验证
- 4 种验证模板 (basic/mechanical/defect/comprehensive)
- 5 种计算属性 (晶格常数/结合能/弹性常数/体模量/空位形成能)
- Dockerfile + docker-compose
- 78/78 测试通过

**阶段 2 (08:00-11:30): 云部署**
- Cloudflare Quick Tunnel 暴露验证服务
- Vercel 自动部署
- 端到端验证通过

**阶段 3 (11:30-12:00): 404 错误修复**
- 根因: 验证服务 SQLite 只有 2 个测试势函数，Supabase 有 44 个
- 修复: 未知势函数自动创建记录

**阶段 4 (12:00-18:00): 架构重构 (核心转折)**
- 从 KIM API + SQLite → LAMMPS + Supabase
- 安装 LAMMPS (conda)
- Supabase verifications 表
- 前端管理后台 (/admin/verify)
- 14 个新测试, 91 total passed

**阶段 5 (18:00-21:30): 域名配置**
- DigitalPlat FreeDomain: nucpot.dpdns.org
- Cloudflare Named Tunnel: verify.nucpot.dpdns.org
- 最终部署架构确定

**产出**: 27 commits, 6712 行新代码, 全链路打通

### Day 4 (05-28 周三): 稳定运维

- CI/CD (GitHub Actions + pre-push hook)
- Named Tunnel systemd 自启动
- 参考值 CRUD API
- 参考值 seed 数据 (23 条)
- 运维文档

### Day 5 (05-29 周四): ref-gap-fill 设计

- 基线评估: 9 维 rubric 评分
- PRD v1.0 (22KB)
- 详细设计规范 (23KB)
- 9 个设计决策 (D001-D009)
- 可复用资产审计 (9 直接复用 + 3 需适配 + 7 新建)
- 数据资产盘点: L1 23 / L2 6981 / L3a 14320 / L3b 279

### Day 6 (05-30 周五): ref-gap-fill 实施 (又一个马拉松日)

**Phase 1 (上午): 基础设施 + 快线**
- T1-T8: 基础设施层 (property-mapping, cache-query, 6 适配器, write-ref-value, db-migrate)
- T9-T10: 快线技能 (librarian-search, librarian-extract)
- T11-T13: 编排集成 (ref-gap-fill SKILL 重构, E2E 测试)
- 72/72 单元测试通过

**Phase 2 (下午): 慢线 + 协议 + 部署**
- T14-T23: 慢线回填 + 消息协议 + cron 部署
- 36/36 单元测试通过
- 4 信号采集 cron + 1 慢线周任务

**验证**
- 快线功能测试: 9/9 通过
- 慢线功能测试: 11/11 通过
- PG UNIQUE 约束添加
- 网络拓扑集中化 (docs/network-topology.md)

---

## 三、关键产出物

### 3.1 代码与数据

| 类别 | 数量 | 说明 |
|------|------|------|
| Python 模块 | 14 个 | 缓存查询、适配器、写入、回填、日志、协议 |
| 测试文件 | 14 个 | 108 单元测试 + 20 功能测试 |
| 设计文档 | 6 个 | PRD + 设计规范 + Phase 2 spec + 测试方案 × 2 |
| 项目管理 | 8 个 | STATE/DECISIONS/WORK_LOG/ISSUES/SIGNALS/README + 报告 × 2 |
| 跟踪文件 | 5 个 | MSPOT + STATUS + PARA 笔记 × 3 |

### 3.2 Git 提交统计

| 项目 | Commits | 说明 |
|------|---------|------|
| nucpot 前端 | 18 | Next.js 验证面板 + 管理后台 |
| nucpot-autovc | 9 | FastAPI 验证服务 |
| ref-gap-fill (workspace) | 20+ | 全部基础设施 + 慢线 + 测试 |

### 3.3 测试覆盖

| 层级 | 数量 | 通过率 |
|------|------|--------|
| 单元测试 (Phase 1) | 72 | 100% |
| 单元测试 (Phase 2) | 36 | 100% |
| 快线功能测试 | 9 | 100% |
| 慢线功能测试 | 11 | 100% |
| **总计** | **128** | **100%** |

---

## 四、经验教训

### 4.1 架构决策

#### ✅ 做对的

**1. 快慢线分离**
快线秒级响应验证需求，慢线周级批量积累数据。这个分离让系统在数据不完整时仍可用，而不是等待所有数据就绪。实际效果：快线 9/9 测试通过时 PG 只有 23 条数据。

**2. 三级缓存逐级扩大**
L1(PG 23条) → L2(NFMD 43条) → L3(llm-wiki 68条 + ontofuel 279属性)。每级命中率递增，总覆盖从 20% 到理论 150%。

**3. 分级写入策略**
high confidence 自动写入，medium/low 标记待审核。避免了"全人工审核太慢"和"全自动太危险"的两难。

**4. 多智能体职责分离**
nucpot-db 专注数据/编排，nucpot-librarian 专注搜索/提取。每个 agent 的 SKILL.md 清晰定义了能力和边界。

**5. 本地 PG + 慢线双写 NFMD**
快线写入本地 PG 保证低延迟，慢线异步双写到 NFMD 保证数据共享。两个存储系统各有用途不冲突。

#### ❌ 做错的 / 后来修正的

**1. KIM API → LAMMPS 重构 (05-27)**
初始选了 KIM API 作为计算引擎，但 Supabase 中 0 个 KIM 格式势函数、49 个 EAM/LAMMPS 格式。**根因: 没有先分析实际数据格式就选了技术栈。** 花了约 2 小时重构。

**教训: 先分析数据，再选技术栈。** 这个错误让 05-27 的"阶段 4"变成了全天最耗时的阶段。

**2. SQLite → Supabase 数据不同步 (05-27)**
验证服务用本地 SQLite 存势函数，前端用 Supabase。用户看到的势函数和验证服务计算的不是同一批。404 错误只是表象，根因是两个数据源不统一。

**教训: 单一数据源原则。** 计算服务直接读 Supabase REST API，不再维护本地副本。

**3. Quick Tunnel → Named Tunnel (05-27)**
先用 Quick Tunnel 暴露验证服务（临时 URL，重启即变），后换成 Named Tunnel（固定 URL）。多走了一步。

**教训: 确定长期使用时直接用 Named Tunnel，不要先用临时方案再迁移。**

**4. nfmd-postgres 端口冲突 (05-30)**
5432 端口和 nucpot-nucpot-db-1 冲突。重建容器改用 15432。

**教训: Docker 容器端口规划应在部署前做冲突检查，建立集中维护文档。**

**5. backfill_l1 "写入" 的语义混淆 (05-30)**
慢线功能测试初期以为 `backfill_l1()` 会真的写 PG，实际只是评估决策返回 WriteStatus。

**教训: API 命名应准确反映行为。"backfill" 暗示写入，实际只做评估。如果重做，会叫 `evaluate_l1_write()`。**

### 4.2 工程实践

#### ✅ 做对的

**1. dev-pm 技能 6 步流程**
Brainstorming → Writing Plans → Subagent-Driven Dev → Verification → Finishing Branch → WORK_LOG + MEMORY。M 级项目严格走这个流程，确保了可追溯性。

**2. TDD 先测后写**
每个 Python 模块先写测试验证失败，再实现验证通过。108/108 不是事后补的测试，是开发过程中写的。

**3. 子智能体并行执行**
T14-T17 四个子智能体并行运行（ontofuel 扩展、慢线回填、日志、协议），显著缩短了开发时间。

**4. 功能测试分层**
L0 单元(mock) → L1 真实数据 → L2 端到端。先跑只读测试，再跑受控写入，最后跑编排。

**5. 网络拓扑集中化**
`docs/network-topology.md` 作为唯一维护点，TOOLS.md 和 SKILL.md 只引用不重复。端口变更只改一份文件。

**6. PG UNIQUE 约束**
ISSUES.md 记录 → 验证零重复 → ALTER TABLE 添加 → 测试确认。应用层去重 + DB 层约束双重保护。

#### ❌ 需要改进的

**1. 子智能体 TRUNCATE 事故 (05-11，历史教训)**
子智能体误执行 TRUNCATE 导致 NFMD 全部修复回滚。

**教训: 子智能体必须加载 nfmd-db-ops 技能，禁止 TRUNCATE/DROP TABLE/无 WHERE 的 DELETE/UPDATE。** 已写入 TOOLS.md 和 SKILL.md。

**2. git add 误提交数据文件 (04-26，历史教训)**
误提交 290 个数据文件到 Git。

**教训: data/ 目录禁止 git add，.gitignore 已包含规则。** 已写入 TOOLS.md。

**3. L3A 参数文件格式不一致**
llm-wiki 提取的参数 JSON 格式（列表 vs 字典、字段名不统一）导致 S1.9 测试多次修正。

**教训: 知识库 schema 应统一，或 adapter 层做格式归一化。**

### 4.3 项目管理

#### ✅ 做对的

**1. 决策日志 (DECISIONS.md)**
9 个决策完整记录：触发问题、考虑方案、选择、理由、验证状态、失效条件。回头看任何决策都有上下文。

**2. PARA + SGT 跟踪体系**
MSPOT 战略方向 + OKR 可量化进度 + PARA 文件组织。从"脑子记"升级到"系统记"。

**3. 信号采集 cron**
4 个 cron job (zombie 清理 / drift 检测 / heartbeat / decision review) 持续监控项目健康。

**4. 工作日志 (WORK_LOG.md)**
每天写了什么、多少测试、多少 commits、遇到什么 bug。不依赖记忆。

#### ❌ 需要改进的

**1. 初期缺少项目管理结构**
05-25~05-27 的开发没有 MSPOT/OKR 跟踪，靠的是密集的飞书沟通和 daily memory。到 05-30 才建立正式跟踪体系。

**教训: 项目启动时就建立跟踪，不要等"有时间再整理"。**

**2. 专家审查环节缺失**
设计规范中提到"待专家审查"，但实际跳过了，直接用功能测试替代。

**教训: 学术项目的数据质量需要领域专家审核，自动化测试不能完全替代。**

---

## 五、数据资产现状

### 5.1 reference_values (L1)

| 体系 | 条数 | 覆盖物性 |
|------|------|---------|
| U (BCC) | 5 | C11, C12, C44, lc, vacancy_E |
| Mo (BCC) | 5 | C11, C12, C44, lc, vacancy_E |
| Zr | 4 | lc, vacancy_E, ... |
| Zr (BCC) | 1 | lc |
| U-Mo (BCC) | 3 | C11, C12, lc |
| Nb | 5 | C11, C12, C44, lc, vacancy_E |
| **合计** | **23** | 目标 112 |

### 5.2 缺口分析

| 优先级 | 缺口数 | 典型体系 |
|--------|--------|---------|
| P1 | 25 | U, Mo, Zr, Nb, U-Mo |
| P2 | 40 | U-Zr, U-Pu-Zr, U-Pu |
| P3 | 24 | Fe, Cr, SiC, UN |
| **合计** | **89** | 假阳性 = 0 |

### 5.3 NFMD parameters (L2)

43 条参数，覆盖 Hf/Nb/Ti/U/U-20Mo 等体系，主要是密度和力学性能。**缺弹性常数。**

---

## 六、下一步与待办

### 短期 (1-2 周)

| # | 任务 | 优先级 | 说明 |
|---|------|--------|------|
| 1 | 慢线 cron 首次运行验证 | P1 | 下周一 09:00 自动触发 |
| 2 | NFMD 弹性常数数据回填 | P2 | 当前 0 条 |
| 3 | adapter_nfmd 补充必填字段 | P2 | id/category/value_type |
| 4 | 前端改进 (分页/筛选/对比) | P2 | 05-26 评审发现的 14 条 |
| 5 | U-Mo C44 = 49.52 GPa 正式写入 PG | P3 | L3.2 提取结果 |

### 中期 (1-2 月)

| # | 任务 | 说明 |
|---|------|------|
| 6 | reference_values 覆盖率 23→100+ | 持续运行快线+慢线 |
| 7 | 更多势函数文件上传 | 当前 .eam.alloy 文件不足 |
| 8 | 前端 E2E 自动化测试 | Playwright |
| 9 | 验证服务 systemd 化 | 进程管理稳定性 |

### 长期

| # | 方向 | 说明 |
|---|------|------|
| 10 | 多尺度模拟集成 | DFT → MD → CALPHAD → Phase-field → BISON |
| 11 | 用户贡献机制 | 允许研究人员提交/审核参考值 |
| 12 | 国际化 | 英文界面 + 多语言支持 |

---

## 七、总结性评估

### 7.1 投入产出

| 指标 | 值 |
|------|-----|
| 开发天数 | 6 天 (其中 2 个马拉松日) |
| 代码量 | ~6700 行 (前端+后端) + ~1200 行 Python (ref-gap-fill) |
| 测试 | 128 个，100% 通过率 |
| 自动化覆盖率 | 快线: 5s 响应, 慢线: 周级积累 |
| 数据覆盖率 | 20% (23/112)，目标 100% |

### 7.2 核心成就

1. **从 0 到 1 建立了完整的验证工作流**: 前端 → 验证服务 → LAMMPS 计算 → 参考值对比 → 结果展示
2. **自动化参考值补全系统**: 多智能体协作，三级缓存，快慢线分离
3. **128 个测试零回归**: TDD 实践证明了"先测后写"的价值
4. **公网可访问**: nucpot.dpdns.org + verify.nucpot.dpdns.org 全球可达

### 7.3 最大风险

1. **ThinkStation 单点依赖**: 所有计算和数据都在一台机器上
2. **数据覆盖率仍低**: 20% 的覆盖率意味着大部分验证请求会 MISS
3. **慢线未经实战**: cron 首次运行尚未发生

---

*本总结基于 05-25~05-30 的 daily memory、WORK_LOG、DECISIONS、测试报告和 PARA 笔记综合编写。*
