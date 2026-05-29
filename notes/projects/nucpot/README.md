# NucPot — 核材料原子间势函数开放平台

## 基本信息

- **仓库**: GitHub Etoile04/nucpot
- **线上地址**: https://nucpot.dpdns.org
- **验证服务**: https://verify.nucpot.dpdns.org
- **开发周期**: 2026-05-25 ~ 进行中
- **状态**: Phase 4 进行中 (T1-T6 完成，ref-gap-fill 设计完成待审查)

## 技术栈

| 层 | 技术 |
|---|------|
| 前端 | Next.js 15 (App Router) + Tailwind CSS |
| 后端 | Supabase Cloud (数据库 + Auth + Storage) |
| 验证服务 | Python FastAPI + LAMMPS (ThinkStation) |
| 部署 | Vercel (CDN) + Cloudflare Named Tunnel |
| 域名 | nucpot.dpdns.org (DigitalPlat FreeDomain) |

## 当前进度

### Phase 1: 基础平台 ✅
- 12 个页面、18 个 API 端点
- 54 个已发布势函数

### Phase 2: 验证管线 ✅
- 4 种验证模板、5 种计算属性
- LAMMPS 计算后端、进度实时查询

### Phase 3: 云部署 ✅
- Vercel + Cloudflare CDN + Named Tunnel
- Supabase Storage 文件上传

### Phase 4: 基础设施自动化 🔄

**T1-T6 基础设施 (已完成 ✅)**
- [x] CI/CD (GitHub Actions + pre-push hook, 42 测试全过)
- [x] Named Tunnel systemd 自启动
- [x] 参考值 CRUD API
- [x] 参考值 seed 数据 (23 条)
- [x] 运维文档

**ref-gap-fill 参考值补全系统 (设计完成，待审查 🔍)**
- [x] PRD v1.0
- [x] 多智能体架构设计 (nucpot-db + nucpot-librarian)
- [x] 详细设计 spec (消息 schema + 文件清单 + 错误处理)
- [x] 可复用资产审计 (节省约 40% 工期)
- [ ] 专家审查 → 更新 spec
- [ ] Phase A: 基础设施实施
- [ ] Phase B/C: 快线/慢线实施
- [ ] Phase D: 编排集成 + E2E 测试

详见 → [ref-gap-fill 项目页](ref-gap-fill.md)

**待完成 🔲**
- [ ] 更多势函数文件上传
- [ ] 前端 E2E 自动化测试

## 关键经验教训

1. **先分析数据再选技术栈** — KIM API → LAMMPS 的重构延误 4h
2. **本地构建成功 ≠ 部署成功** — TS 类型错误导致 Vercel 静默失败 28h
3. **部署后必须验证** — 检查 age header 归零
4. **Quick Tunnel vs Named Tunnel** — 确定长期使用时直接用 Named Tunnel

## 关键配置

| 配置项 | 值 |
|--------|-----|
| Cloudflare Tunnel | `nucpot-verify` (b6872742-...) |
| ThinkStation SSH | `z203@100.70.30.21` |
| LAMMPS 路径 | `~/anaconda3/bin/lmp_serial` |
| 环境变量 | `NEXT_PUBLIC_AUTOCV_API_URL=https://verify.nucpot.dpdns.org` |

## 相关文档

- [架构设计](architecture.md)
- [ref-gap-fill 项目](ref-gap-fill.md) — 参考值补全系统
- [开发经验教训](../../resources/nucpot/dev-lessons.md)
- [ref-gap-fill 可复用资产审计](../../resources/ref-gap-fill-reuse-audit.md)
- [开发测试报告 2026-05-29](https://my.feishu.cn/docx/C0h2dBJ1WoxRolxiixncDbNHnlc) (飞书云文档)
