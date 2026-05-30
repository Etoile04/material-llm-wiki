# Ref-Gap-Fill 问题追踪

| # | 问题描述 | 状态 | 创建日期 | 备注 |
|---|---------|------|---------|------|
| 1 | ontofuel 本体缺少 C11/C12/C44/C33 属性定义 | 🟢已解决 | 2026-05-29 | T14 扩展完成 |
| 2 | nucpot-db / nucpot-librarian agent 配置未添加到 openclaw.json | 🟢已解决 | 2026-05-30 | T21 添加完成 |
| 3 | wiki adapter confidence 类型不一致 (float vs string) | 🟢已解决 | 2026-05-30 | commit `0fdfc4f` |
| 4 | 慢线 (子项目 C) 未实现 | 🟢已解决 | 2026-05-30 | T15-T22 完整实现 |
| 5 | T6 完成事件丢失 (session yield) | 🟢已解决 | 2026-05-30 | 通过直接跑测试确认 |
| 6 | gitignore 排除 data/ 导致 property-mapping.json 不追踪 | 🟢已解决 | 2026-05-30 | 添加 `!data/property-mapping.json` 例外 |
| 7 | 慢线 L2 Supabase 实际写入未实现 | 🟡处理中 | 2026-05-30 | 格式转换已完成，INSERT 标记 TODO |
| 8 | PG reference_values 缺 UNIQUE constraint (element_system, phase, property, method, source) | 🟡待解决 | 2026-05-30 | L2.4 发现：重复写入未被 DB 拦截，应用层有去重但 DB 层无保护 |
