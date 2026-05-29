# NucPot 项目笔记

## 项目概述
NucPot 是面向核材料研究者的原子间势函数开放平台，属于 OBJ4（核材料势函数库建设）的技术实现。

## 关键架构决策

### 为什么选 Next.js + Supabase
- **Next.js App Router**: SSR + 客户端路由，适合势函数详情页 SEO
- **Supabase**: 开箱即用的 Auth + PostgreSQL + RLS，减少后端开发量
- **JSONB + GIN**: 势函数的 applicability/references/extra 等半结构化数据天然适合 JSONB

### 为什么不做势函数文件托管
- 势函数文件受作者版权保护，NIST IPR/OpenKIM 也仅做索引
- 改为外部链接引导（NIST IPR 下载页 + 论文 DOI + OpenKIM）
- 用户上传时需要版权授权声明（三选一）+ 授权文件

### 数据库设计要点
- `potentials` 表: JSONB 字段存储灵活元数据
- `profiles` + `contributions`: Auth + 贡献追踪
- RLS 策略: anon 只读, 认证用户可上传, admin 可审核
- `file_url` 字段预留但当前为空（等有授权文件后启用）

## 代码模式

### Supabase 客户端
```ts
// 普通客户端（受 RLS 保护）
export const supabase = createClient(url, anonKey)

// Admin 客户端（绕过 RLS，仅服务端使用）
export const supabaseAdmin = createClient(url, serviceRoleKey)
```

### Auth Provider 模式
- `AuthProvider.tsx` 包裹 layout.tsx
- `useAuth()` 提供 user/profile/session/signIn/signUp/signOut
- Nav 根据 auth 状态显示不同菜单

### 测试策略
- Vitest + jsdom 单元测试（直接调用 route handler）
- Puppeteer 集成测试（需要 dev server 运行）
- Auth 测试 skip（需要真实 Supabase）

## 性能数据
- 构建: ~1.7s (Turbopack)
- 测试: ~700ms (17 tests)
- 势函数数量: 50
- 元素覆盖: 15+ 种
- 势函数类型: EAM/MEAM/Buckingham/Tersoff/AIREBO/LJ/RANN/ML
