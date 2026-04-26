# Zhang et al. 2025 — 基于机器学习的铀合金腐蚀替代材料智能筛选模型

## Metadata
- **标题**: Intelligent screening model for uranium alloy corrosion substitute alloys based on machine learning
- **作者**: Wanying Zhang, Xiaoyuan Wang, Yibo Ai, Weidong Zhang
- **机构**: 北京科技大学 国家材料服役安全科学中心
- **期刊**: Progress in Natural Science: Materials International, 35 (2025) 622–630
- **DOI**: 10.1016/j.pnsc.2025.03.016
- **关键词**: Uranium alloys, Alternative alloys, Machine learning, LSTM, PSO

## 研究方法

本研究旨在为 U-2.5 wt%Nb 铀合金寻找氧化性能相似的替代合金，以降低放射性材料的实验风险与成本。方法分三个阶段：

1. **特征筛选**：基于 227 条 U-2.5Nb 氧化数据和 1265 条 25 种候选合金的腐蚀数据，使用 Extremely Randomized Trees 分类器进行特征重要性排序，确定温度和时间为氧化行为的主要影响因素（Gini 重要性分别为 0.060 和 0.055）。

2. **图像聚类与相似度筛选**：采用 AP（Affinity Propagation）聚类算法将 21 种合金按氧化动力学曲线聚类为 4 类，选定与 U-2.5Nb 最相近的第 3 类（16 种 Fe-Cr-Ni 系合金）。进一步使用 K-means 图像聚类（图像尺寸 496×369 像素）和 VGG16 卷积神经网络提取特征向量，通过余弦相似度比较，最终从 25 种合金中筛选出 9 种氧化动力学曲线相似的替代合金（相似度阈值 ≥ 0.916）。

3. **PSO-LSTM 生成替代合金**：以 9 种筛选合金的化学元素质量分数和温度为训练数据，构建 PSO-LSTM 模型预测替代合金成分。PSO 优化 LSTM 的神经元数和学习率，输入为氧化时间与氧化增重，输出为合金元素组成。

## 主要发现

- PSO 优化后 LSTM 最优参数：**神经元数 = 64，学习率 = 0.03**
- 模型性能：**MAE = 0.850，R² = 0.959**
- 筛选的 9 种替代合金包括 Fe-Cr-Ni、Ce、Ce-5La、Inconel 600、GX40CrNiSi25-12、310S、Co-20Ni-5Al、AlCoCrFeNi 等
- 实验验证：在 333K（对应替代合金 1423K）条件下，生成替代合金与 U-2.5Nb 氧化动力学曲线的**总体相似度达到 80%**
- 训练集占比 80% 时模型拟合最优，低于 80% 欠拟合，高于 80% 过拟合

## Key Equations

### LSTM 六步更新公式

**Eq.1 — 候选记忆状态：**
$$\tilde{c}_t = \tanh(W_{xc} x_t + W_{hc} h_{t-1} + b_c)$$
其中 $W_{xc}$ 为输入到记忆细胞的权重，$W_{hc}$ 为循环权重矩阵，$h_{t-1}$ 为前一时刻隐藏状态，$b_c$ 为记忆节点偏置。

**Eq.2 — 输入门：**
$$i_t = \sigma(W_{xi} x_t + W_{hi} h_{t-1} + b_i)$$
调控当前输入数据对记忆模块整体状态的影响。

**Eq.3 — 遗忘门：**
$$f_t = \sigma(W_{xf} x_t + W_{hf} h_{t-1} + b_f)$$
决定历史数据对当前记忆细胞状态的影响，用于丢弃无关信息。

**Eq.4 — 记忆细胞状态更新：**
$$c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$$
遗忘门与输入门交互，共同调节旧信息的丢弃与新状态信息的融入。

**Eq.5 — 输出门：**
$$o_t = \sigma(W_{xo} x_t + W_{ho} h_{t-1} + b_o)$$

**Eq.6 — 隐藏层输出：**
$$h_t = o_t \odot \tanh(c_t)$$

### PSO-LSTM 模型结构

- **输入**: 氧化时间 + 氧化增重（14 组合金动力学曲线）
- **输出**: 合金各元素质量分数 + 实验温度
- **PSO 参数**: 粒子数 = 20，搜索次数 = 30，优化目标为 MSE 最小化；待优化参数为 batch size（10–60）、epoch（5–200）、step（3–30）；惯性权重范围 [0.2, 0.8]，学习因子 $G = c_2$
- **LSTM 内部优化器**: Adam（学习率 0.001）
- **参数初始化**: Xavier 正态初始化（权重）+ 零偏置

## Related Work
- [[wiki/summaries/2026_AcceleratedDesign_ThermalStability_UMo|2026_AcceleratedDesign_ThermalStability_UMo]] — 同为机器学习辅助铀合金设计
- [[wiki/summaries/2025_Zhang_ML_UraniumAlloy_CorrosionScreening|2025_Zhang_ML_UraniumAlloy_CorrosionScreening]] — PSO-LSTM合金筛选
- [[wiki/summaries/Lu_2018_CALPHAD_UFuels|Lu_2018_CALPHAD_UFuels]] — CALPHAD方法评估铀合金热力学
- [[wiki/entities/FuelAlloy|FuelAlloy]] — 铀合金燃料设计
