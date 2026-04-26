# ERR-20260421-001: Batch D 目录名与内容不匹配 + MinerU 重转失败

> **日期**: 2026-04-21  
> **严重程度**: P1（影响数据准确性）  
> **涉及**: llm-wiki SKILL.md, MinerU 转换流程

---

## 错误描述

### 错误 A：3/9 篇文献目录名与实际内容不匹配

| 目录名（MinerU 自动生成） | 实际内容 |
|--------------------------|---------|
| `Interdiffusion Between Zr Diffusion Barrier and U-Mo Alloy_6dfb90c4` | Beeler et al. 2020 "Radiation driven diffusion in γ U-Mo" |
| `TRANSFORMATION CHARACTERISTICS OF U-Mo AND U-Mo-Ti ALLOYS_b2a56895` | Aagesen et al. 2025 "Void superlattice in Mo" |
| `Yun 等 - Investigation of swelling behaviors of U-10Zr meta` | Qian et al. 2022 "Cavitational void swelling of U-10Zr" |

**影响**：提取任务按目录名分发，子智能体需额外判断实际内容，浪费 tokens 和时间。

### 错误 B：MinerU 重转 SSL 失败

**错误**: `SSLError: [SSL: UNEXPECTED_EOF_WHILE_READING]` 连接 `huggingface.co`

**根因链**:
1. HuggingFace 在国内网络不可达（curl 测试返回 000）
2. 未配置 HF Mirror 环境变量（`HF_ENDPOINT`）
3. MinerU 模型缓存目录无 PDF-Extract-Kit 模型 → 每次启动尝试下载
4. 首次转换可能用其他网络环境成功，后续重转因网络变化失败

---

## 5-Why 分析

### 错误 A：目录名不匹配

1. **为什么目录名不匹配？** → MinerU 从 PDF 文件名生成目录名，但 Zotero 存储的文件名可能是错的
2. **为什么 Zotero 文件名错？** → Zotero 自动下载时用元数据命名，元数据可能不完整或被覆盖
3. **为什么没有提前发现？** → 转换后未校验"目录名 vs PDF 实际内容"的一致性
4. **为什么没有校验流程？** → SKILL.md ingest 流程缺少"源文件身份验证"步骤
5. **为什么技能设计时没考虑？** → 假设 PDF 文件名可靠，未做防御性设计

### 错误 B：MinerU 重转失败

1. **为什么重转失败？** → SSL 无法连接 HuggingFace
2. **为什么需要连 HuggingFace？** → 本地无模型缓存
3. **为什么无缓存？** → 首次转换可能在其他环境（VPN/代理）下完成
4. **为什么没有离线模式？** → 未配置 `HF_HUB_OFFLINE=1` 或镜像源
5. **为什么没提前检查？** → SKILL.md 未要求在批量转换前验证模型可用性

---

## 改进措施

### 技能层面（SKILL.md 修改）

#### 1. 新增"源文件身份验证"步骤（ingest 流程第 0 步）

```markdown
### 0. 源文件验证（Pre-ingest Check）
1. 读取 MD 文件前 50 行，提取论文标题
2. 与目录名/文件名对比
3. 如不匹配：
   - 以 MD 内容中的标题为准
   - 更新 slug 为实际论文的 `YYYY_Author_Title` 格式
   - 记录不匹配到 log
```

#### 2. 新增"MinerU 环境检查"步骤

```markdown
### MinerU 转换前检查
1. 验证模型可用性：
   ```bash
   HF_HUB_OFFLINE=1 ~/.openclaw/workspace/.venv-mineru/bin/mineru --help 2>&1 | head -3
   ```
2. 如失败，尝试配置镜像：
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```
3. 如仍失败，使用 pdftotext 兜底并记录
```

#### 3. 目录命名规范化

```markdown
### 目录命名规范
- 转换完成后，自动重命名为 `YYYY_Author_ShortTitle` 格式
- 基于内容提取标题，而非依赖原始文件名
- 保留原始文件名映射到 `raw/mineru/_name_mapping.json`
```

#### 4. 批量转换增加容错

```markdown
### 批量转换容错策略
1. MinerU 失败 → pdftotext 兜底（自动）
2. pdftotext 也失败 → 跳过并记录到 `raw/mineru/_failed_conversions.json`
3. 每次转换后验证公式覆盖率：
   ```bash
   grep -c '\$\$' output.md  # 模型类论文应 > 5
   grep -c 'Formula Recognition.*Disabled' output.md  # 应为 0
   ```
```

### 脚本层面

#### 5. 创建 `scripts/verify_source_identity.py`

- 输入：MD 文件路径
- 读取前 50 行提取标题
- 与目录名/预期 slug 对比
- 输出：匹配/不匹配报告 + 建议的正确 slug

#### 6. 创建 `scripts/check_mineru_env.sh`

- 检查 MinerU 二进制
- 检查模型缓存
- 测试 HF 连接（或镜像）
- 输出：环境就绪/需修复

#### 7. 配置 HF 镜像

```bash
# 在 SKILL.md 或 TOOLS.md 中记录
export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_OFFLINE=1  # 有缓存时优先离线
```

---

## 预防规则

1. ⛔ **永不信任 PDF 文件名** — 始终从 MD 内容提取标题验证
2. ✅ **转换前检查环境** — MinerU 可用性、模型缓存、网络连接
3. ✅ **转换后验证输出** — 公式覆盖率、内容完整性
4. ✅ **离线优先** — 配置 HF 镜像和离线模式
5. ✅ **兜底方案** — pdftotext + web_search 补充公式

---

## 行动项

| 优先级 | 行动 | 预计时间 |
|--------|------|---------|
| P0 | 配置 HF 镜像环境变量 | 5 min |
| P0 | 创建 `check_mineru_env.sh` | 10 min |
| P1 | SKILL.md 新增源文件验证步骤 | 15 min |
| P1 | SKILL.md 新增 MinerU 环境检查 | 10 min |
| P2 | 创建 `verify_source_identity.py` | 20 min |
| P2 | 整理已有目录的 `_name_mapping.json` | 15 min |

---

*记录时间: 2026-04-21 13:00 CST*
