# SpatialGlue（Nature Methods 2024）文献资料

## 基本信息

- **论文题目：** Deciphering spatial domains from spatial multi-omics with SpatialGlue
- **作者：** Long Y. 等
- **发表来源：** Nature Methods，21，1658–1667，2024
- **DOI：** https://doi.org/10.1038/s41592-024-02316-4
- **论文链接：** https://www.nature.com/articles/s41592-024-02316-4
- **开放全文：** https://pmc.ncbi.nlm.nih.gov/articles/PMC11399094/

## 研究问题

SpatialGlue 主要解决同一组织切片中多种空间组学模态的联合分析问题，目标是在保留空间背景的同时整合不同模态的信息，以识别组织空间域并分析组织结构特征。

## 方法概述

SpatialGlue 使用图神经网络编码不同模态的空间图和特征图，并通过双重注意力机制进行两阶段融合。第一阶段在单一模态内部整合空间信息与分子特征；第二阶段进一步融合不同模态的表示。论文报告的总目标函数包括重构项和相关性项，并根据不同数据集设置图权重。

## 证据记录

- **SPATIALGLUE2024:E01：双重注意力设计。** 支持模型先进行模态内融合，再进行模态间融合。位置：结果部分“SpatialGlue model structure”，图1及相关文字。
- **SPATIALGLUE2024:E02：图构建。** 支持模型为各模态构建空间邻居图和特征近邻图，并通过图神经网络学习表示。位置：图1及模型结构说明。
- **SPATIALGLUE2024:E03：优化目标。** 支持总损失包含重构项和相关性项。位置：方法部分公式（17）。
- **SPATIALGLUE2024:E04：数据集参数设置。** 支持论文根据不同数据集经验设置图权重等参数。位置：方法部分“Implementation details of SpatialGlue”。

## 阅读分析

SpatialGlue 的特点是通过层次化注意力机制整合空间图、特征图和不同组学模态。其图权重需要结合数据集进行设置，说明模型应用时需要关注数据特征与参数配置之间的关系。该点属于实际应用层面的分析，不应夸大为作者明确声明的模型缺陷。
