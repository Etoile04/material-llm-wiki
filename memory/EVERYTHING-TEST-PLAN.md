# Everything Claude Code 测试计划

## 测试环境

- Claude Code 版本: 2.1.31
- Everything 插件: 已安装
- 需要 API keys: **否**（本地配置）
- 测试日期: 2026-02-06

## 测试策略

根据 README，Everything plugin 包含：
- ✅ 15+ agents
- ✅ 30+ skills
- ✅ 20+ commands
- ✅ Hooks 系统
- ✅ Rules 系统

**注意**: 不需要 API keys，所有功能基于本地配置。

---

## 命令测试列表

### Category 1: 开发工作流命令 (核心)

#### 1.1 `/plan` - 实现规划
```bash
claude -p "/plan 'Add user authentication feature'"
```
**预期**: 生成详细的实现计划，包括步骤和技术选择
**验证**: 计划是否合理，是否包含必要的步骤

#### 1.2 `/tdd` - 测试驱动开发
```bash
claude -p "/tdd 'Add a function to validate email addresses'"
```
**预期**: 按照红-绿-重构流程生成代码
**验证**: 测试用例先编写，然后实现代码

#### 1.3 `/e2e` - E2E 测试生成
```bash
claude -p "/e2e 'User login and logout flow'"
```
**预期**: 生成完整的端到端测试用例
**验证**: 覆盖主要用户流程

#### 1.4 `/code-review` - 代码审查
```bash
claude -p "/code-review Review the authentication module"
```
**预期**: 提供质量、安全性、可维护性反馈
**验证**: 发现潜在问题并给出改进建议

#### 1.5 `/build-fix` - 修复构建错误
```bash
# 先创建一个有错误的文件
claude -p "/build-fix Fix the build errors"
```
**预期**: 分析构建错误并提供修复方案
**验证**: 错误被修复，构建成功

#### 1.6 `/refactor-clean` - 清理死代码
```bash
claude -p "/refactor-clean Remove unused imports and dead code"
```
**预期**: 识别并移除未使用的代码
**验证**: 代码精简，功能保持不变

---

### Category 2: 学习和验证命令

#### 2.1 `/learn` - 提取模式
```bash
claude -p "/learn Extract the patterns from our discussion about React hooks"
```
**预期**: 从当前会话提取可重用的模式
**验证**: 模式准确，可以复用

#### 2.2 `/checkpoint` - 保存验证状态
```bash
claude -p "/checkpoint Save the current state as verification checkpoint"
```
**预期**: 保存当前代码和状态
**验证**: 状态可以恢复

#### 2.3 `/verify` - 运行验证循环
```bash
claude -p "/verify Run the verification loop against saved checkpoint"
```
**预期**: 比较当前状态与检查点
**验证**: 发现差异并报告

---

### Category 3: Continuous Learning v2 命令

#### 3.1 `/instinct-status` - 查看学习到的本能
```bash
claude -p "/instinct-status"
```
**预期**: 列出所有学习到的本能及其置信度
**验证**: 本能列表显示，置信度合理

#### 3.2 `/instinct-import` - 导入本能
```bash
# 创建一个测试本能文件
cat > test-instinct.json << 'EOF'
{
  "instincts": [
    {"pattern": "use useEffect with dependencies", "confidence": 0.9}
  ]
}
EOF

claude -p "/instinct-import test-instinct.json"
```
**预期**: 导入指定的本能文件
**验证**: 本能已添加到系统

#### 3.3 `/instinct-export` - 导出本能
```bash
claude -p "/instinct-export Export all learned instincts"
```
**预期**: 导出所有本能到文件
**验证**: 文件包含正确的本能数据

#### 3.4 `/evolve` - 将本能聚类为技能
```bash
claude -p "/evolve Cluster related instincts into skills"
```
**预期**: 将相关的本能组织成技能
**验证**: 生成的技能逻辑清晰，可重用

---

### Category 4: Go 语言支持命令

#### 4.1 `/go-review` - Go 代码审查
```bash
# 创建一个测试 Go 文件
cat > test.go << 'EOF'
package main

func main() {
    fmt.Println("Hello")
}
EOF

claude -p "/go-review Review test.go"
```
**预期**: Go 特定的代码审查
**验证**: 指出 Go 惯用法和潜在问题

#### 4.2 `/go-test` - Go TDD 工作流
```bash
claude -p "/go-test Write tests and implementation for a Go function"
```
**预期**: Go TDD 流程（测试先行）
**验证**: Go 测试格式正确，实现通过

#### 4.3 `/go-build` - 修复 Go 构建错误
```bash
# 创建有错误的 Go 代码
cat > error.go << 'EOF'
package main

func bad() {
    return
}
EOF

claude -p "/go-build Fix the Go build errors"
```
**预期**: 修复 Go 构建错误
**验证**: Go 代码编译通过

---

### Category 5: 技能和配置命令

#### 5.1 `/skill-create` - 从 git 生成技能
```bash
claude -p "/skill-create"
```
**预期**: 分析当前 git 历史，生成 SKILL.md
**验证**: 生成的技能准确反映项目模式

#### 5.2 `/skill-create --instincts` - 生成技能和本能
```bash
claude -p "/skill-create --instincts"
```
**预期**: 同时生成技能和本能
**验证**: 两部分都有用

#### 5.3 `/setup-pm` - 配置包管理器
```bash
claude -p "/setup-pm"
```
**预期**: 检测并配置包管理器
**验证**: 配置正确的包管理器（npm/pnpm/yarn/bun）

---

## 测试项目

使用现有的英语单词卡项目进行测试：
```bash
cd /Users/lwj04/clawd/english-flashcards
```

---

## 测试执行计划

### Phase 1: 基础命令测试 (优先级：高)

1. `/plan` - 测试规划功能
2. `/tdd` - 测试 TDD 工作流
3. `/code-review` - 测试代码审查
4. `/build-fix` - 测试错误修复

### Phase 2: 学习和验证 (优先级：中)

5. `/learn` - 测试模式提取
6. `/checkpoint` - 测试状态保存
7. `/verify` - 测试验证循环

### Phase 3: Continuous Learning v2 (优先级：中)

8. `/instinct-status` - 查看本能
9. `/instinct-import` - 导入本能
10. `/instinct-export` - 导出本能
11. `/evolve` - 聚类本能

### Phase 4: Go 支持 (优先级：低，除非使用 Go)

12. `/go-review` - Go 代码审查
13. `/go-test` - Go TDD
14. `/go-build` - Go 构建修复

### Phase 5: 高级功能 (优先级：低)

15. `/skill-create` - 技能生成
16. `/e2e` - E2E 测试
17. `/refactor-clean` - 代码清理
18. `/setup-pm` - 包管理器配置

---

## 测试记录模板

```markdown
## 测试结果

| 命令 | 状态 | 耗时 | 说明 |
|--------|------|------|------|
| /plan | ✅ | 5s | 生成了3步计划 |
| /tdd | ✅ | 12s | 生成了测试和实现 |
| ... | ... | ... | ... |

### 问题记录

1. **命令**: `/instinct-status`
   - **问题**: 没有找到本能文件
   - **解决方案**: 需要先运行 `/learn` 或 `/instinct-import`

### 成功的功能

- ✅ `/plan` 生成了合理的实施计划
- ✅ `/tdd` 遵循了红-绿-重构流程

### 改进建议

1. `/learn` 的提取质量可以更高
2. `/skill-create` 需要更多的 git 历史才能生成好的技能
```

---

## 下一步

1. **准备测试环境**
   - 确认 Everything plugin 已正确安装
   - 准备测试项目（english-flashcards）
   - 创建测试文件和数据

2. **执行测试**
   - 按 Phase 1-5 顺序执行
   - 记录每个命令的结果
   - 截图或保存输出

3. **分析结果**
   - 总结成功和失败的命令
   - 记录问题和解决方案
   - 评估整体可用性

4. **编写测试报告**
   - 创建详细的测试报告
   - 更新学习笔记
   - 分享发现和经验

---

*创建日期: 2026-02-06*
*预计完成: 2026-02-06*
