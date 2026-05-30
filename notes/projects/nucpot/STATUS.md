# NucPot 项目 OKR 进度看板

> 更新时间: 2026-05-30
> 季度: 2026 Q2

## MSPOT 战略

### Mission (使命)
构建核材料势函数验证的自动化基础设施，实现参考物性值的持续自动化补全。

### Strategy (策略)
快慢线分离 + 多智能体协作 + 三级缓存。快线实时响应（秒级），慢线批量积累（周级）。

### Projects (项目, ≤5)
1. **ref-gap-fill** — 参考值补全系统 ← 当前聚焦
2. **势函数验证 API** — FastAPI autovc-api
3. **NFMD 数据库平台** — 材料参数管理

### Omissions (不做)
- ❌ 不做前端 UI（专注后端+自动化）
- ❌ 不做新势函数开发（只验证已有势函数）
- ❌ 不做多尺度模拟集成（Phase 2+ 考虑）

### Success Metrics
- reference_values 覆盖率: 23→100+ 条
- 快线缓存命中率: 0%→50%+
- 自动化补全比例: >80%

---

## OKR 1: ref-gap-fill 参考值自动化补全

**Aligned to**: MSPOT Project #1
**Status**: 🟢 Phase 2 完成

### KR 1.1: 三级缓存查询系统
- **Metric**: 物性映射覆盖率 × 查询正确性
- **Target**: 12 物性 × 3 级缓存全部可查
- **Current**: ✅ 100%
- **Status**: 🟢

### KR 1.2: 快线端到端补全
- **Metric**: 功能测试通过率
- **Target**: 全部通过
- **Current**: ✅ 9/9 (100%)
- **Status**: 🟢

### KR 1.3: 慢线批量回填
- **Metric**: 慢线功能测试通过率
- **Target**: 全部通过
- **Current**: ✅ 11/11 (100%)
- **Status**: 🟢

### KR 1.4: reference_values 覆盖
- **Metric**: 目标体系 × 物性覆盖数
- **Target**: 14 体系 × 8 物性 = 112 条
- **Current**: 23/112 (20.5%)
- **Status**: 🟡 基础设施就绪，需持续运行

### KR 1.5: 代码质量
- **Metric**: 单元测试通过率
- **Target**: 100%
- **Current**: ✅ 108/108 (100%)
- **Status**: 🟢

---

## OKR 2: 势函数验证 API 稳定性

**Aligned to**: MSPOT Project #2
**Status**: 🟡 运行中

### KR 2.1: API 可用性
- **Metric**: 正常运行时间
- **Target**: >95%
- **Current**: 运行中 (ThinkStation Docker)
- **Status**: 🟡

### KR 2.2: reference_values UNIQUE 约束
- **Metric**: 数据完整性保护
- **Target**: DB 层约束已添加
- **Current**: ✅ `uq_ref_value_unique` 已生效
- **Status**: 🟢

---

## OKR 3: NFMD 数据平台

**Aligned to**: MSPOT Project #3
**Status**: 🟡 数据积累中

### KR 3.1: 参数数据量
- **Metric**: parameters 表记录数
- **Target**: 100+ 参数
- **Current**: 43 条
- **Status**: 🟡

### KR 3.2: 弹性常数覆盖
- **Metric**: C11/C12/C44/C33 参数数
- **Target**: 覆盖主要体系
- **Current**: 0 条 (缺弹性常数)
- **Status**: 🔴

---

## 周报摘要

### Week 2026-05-26 ~ 05-30
| 日 | 完成事项 |
|----|---------|
| Thu 05-29 | PRD + 设计规范 + 资产审计 + 设计决策 D001-D004 |
| Sat 05-30 AM | Phase 1 全部完成 (72 tests), dev-pm 6步流程 |
| Sat 05-30 PM | Phase 2 全部完成 (36 tests), 快线 9/9 + 慢线 11/11 |
| Sat 05-30 | PG UNIQUE 约束添加, 网络拓扑集中化, PARA+SGT 跟踪建立 |

**本周产出**: 14 个 Python 模块, 14 个测试文件 (108 tests), 6 个设计文档, 9 个决策, 20 个功能测试

### Next Week Plan
- [ ] 慢线 cron 首次运行验证 (周一 09:00)
- [ ] NFMD 弹性常数数据回填
- [ ] 考虑正式写入 L3.2 提取的 U-Mo C44

---

## Change Log

| 日期 | 变更 |
|------|------|
| 2026-05-30 | 初始版本 — OKR 1-3 建立 |
