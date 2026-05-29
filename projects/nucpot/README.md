# NucPot — 核材料势函数开放平台

**GitHub**: https://github.com/Etoile04/nucpot
**Local**: ~/projects/nucpot
**OBJ4 OKR**: 核材料势函数库建设 (ID: 7639257265102933210)
**Phase**: Phase 4 进行中 (T1-T6 完成 + ref-gap-fill 设计完成待审查)

## KR 进度

| KR | 内容 | 截止 | 状态 | Score |
|----|------|------|------|-------|
| KR1 | 国内外平台调研 | 05-31 | ✅ 完成 | 0.7 |
| KR2 | MVP 原型设计 | 06-15 | ✅ Phase 1+2 完成 | 0.8 |
| KR3 | 团队协作建设 | 06-30 | 🟡 待启动 | 0.1 |
| KR4 | — | — | ⬜ | 0.1 |

## Phase 进度

### Phase 1 — MVP ✅ (05-24 完成)
- 6 页面 + 3 API
- 10 个种子势函数
- 高级检索（元素×类型×温度×核材料标签）
- 暗色主题 UI
- 13 个集成测试

### Phase 2 — 认证与扩展 ✅ (05-24 完成)
- 用户认证（Supabase Auth + RLS + profiles 表）
- 势函数上传 + 社区贡献（含版权授权验证）
- 管理后台（统计 + 贡献审核）
- 50+ 势函数批量扩展（15 种元素体系）
- 授权书模板下载功能
- 势函数详情页外部下载链接

### Phase 3 — 规划中 🔲
- [ ] 在线模拟测试（参考 OpenKIM XtalG）
- [ ] ML 训练数据集模块
- [ ] 100→200+ 势函数扩展
- [ ] 自动化基准测试套件

### Phase 4 — 基础设施自动化 🔄

**T1-T6 基础设施 (已完成 ✅)**
- [x] T1: CI/CD — GitHub Actions + pre-push hook (42 测试全过)
- [x] T2: Named Tunnel systemd 自启动
- [x] T3: 验证服务 reference_values CRUD API
- [x] T4: 参考值 seed 数据 (23 条，5 体系)
- [x] T5: 运维文档
- [x] T6: pre-push hook tsc --noEmit 检查

**ref-gap-fill 参考值补全系统 (设计完成，待审查 🔍)**
- [x] PRD v1.0 (22KB)
- [x] 多智能体架构设计 (nucpot-db + nucpot-librarian)
- [x] 详细设计 spec (消息 schema + 文件清单 + 错误处理)
- [x] 可复用资产审计 (节省约 40% 工期)
- [x] PARA 整理归档
- [ ] 专家审查 → 更新 spec
- [ ] Phase A: 基础设施实施 (property-mapping + cache-query + adapters)
- [ ] Phase B: 快线 (librarian-search/extract SKILL + agent)
- [ ] Phase C: 慢线 (cron + llm-wiki + ontofuel 集成)
- [ ] Phase D: 编排集成 (ref-gap-fill SKILL 重构 + E2E 测试)

### Phase 5 — 远期 🔲
- [ ] KIM API 兼容层
- [ ] 多语言支持
- [ ] 标准草案发布

## 技术栈
- Next.js 16 (App Router) + Tailwind CSS 4
- Supabase (PostgreSQL + Auth + Storage)
- TypeScript, Vitest
- Puppeteer (截图/测试)

## 关键 Commits
- `b3011409` MVP 完成 (Phase 1)
- `13a6df8` Phase 2 完成 (合并)
- `403598a` 版权授权验证
- `d3d4d2a` 授权书模板

## 目录结构
```
~/projects/nucpot/
├── src/app/          # 页面 + API
├── src/components/   # Nav, AuthProvider
├── src/lib/          # supabase.ts, types.ts
├── supabase/         # schema.sql, migrations/
├── scripts/          # seed-db.mjs, expand-potentials.mjs
├── __tests__/        # 测试
├── docs/screenshots/ # UI 截图
├── docs/GUIDE.md     # 使用教程
└── public/           # 静态文件 + 授权模板
```
