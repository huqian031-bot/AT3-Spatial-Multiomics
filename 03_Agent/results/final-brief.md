# 空间多组学整合方法比较研究简报

## 研究问题

空间多组学分析需要同时利用组织空间位置和不同分子模态的信息。本简报比较 PRAGA、SpatialGlue 和 COSMOS 的整合策略，并概括其方法差异。

## 三种方法比较

**PRAGA（AAAI 2025）**：为不同组学学习特征图，并与空间邻接关系结合形成自适应聚合图；通过 GCN 提取模态表示，再利用贝叶斯高斯混合模型及簇分裂、合并机制调整原型，开展动态原型对比学习。[PRAGA2025:E01] [PRAGA2025:E02] [PRAGA2025:E03]

**SpatialGlue（Nature Methods 2024）**：为各模态构建空间图和特征图，使用双重注意力机制先进行模态内融合，再进行模态间融合；优化目标包括重构项和相关性项。[SPATIALGLUE2024:E01] [SPATIALGLUE2024:E02] [SPATIALGLUE2024:E03]

**COSMOS（Nature Communications 2025）**：使用模态专属 GCN 编码器提取表示，通过 WNN 权重整合模态，并采用 DGI 风格的局部—全局对比目标及空间正则化。[COSMOS2025:E01] [COSMOS2025:E02] [COSMOS2025:E03]

## 综合比较

三种方法的主要区别在于融合机制：PRAGA 强调动态图和动态原型的自适应学习；SpatialGlue 强调基于双重注意力的层次化融合；COSMOS 强调模态权重与局部—全局表示学习。三篇论文的数据平台、组织类型、模态组合和评价流程并不完全相同，因此不能仅依据各自报告的 ARI 或 NMI 直接排列方法优劣。

## 结论与启示

后续方法比较应尽量统一数据集、预处理和聚类读出，并同时考察聚类指标、空间边界、空间连续性和运行效率。COSMOS 关于模拟数据仅使用基因表达谱的说明针对其模拟设计，不应扩大解释为其真实数据实验仅使用单一模态。[COSMOS2025:E04]

## 参考文献

1. Huang X. 等（2025）. PRAGA: Prototype-aware Graph Adaptive Aggregation for Spatial Multi-modal Omics Analysis. *AAAI*, 39(1), 326–333. https://doi.org/10.1609/aaai.v39i1.32010
2. Long Y. 等（2024）. Deciphering spatial domains from spatial multi-omics with SpatialGlue. *Nature Methods*, 21, 1658–1667. https://doi.org/10.1038/s41592-024-02316-4
3. Zhou Y. 等（2025）. Cooperative integration of spatially resolved multi-omics data with COSMOS. *Nature Communications*, 16, 27. https://doi.org/10.1038/s41467-024-55204-y
