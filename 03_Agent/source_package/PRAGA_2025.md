# PRAGA（AAAI 2025）文献资料

## 基本信息

- **论文题目：** PRAGA: Prototype-aware Graph Adaptive Aggregation for Spatial Multi-modal Omics Analysis
- **作者：** Huang X. 等
- **发表来源：** Proceedings of the AAAI Conference on Artificial Intelligence，39(1)，326–333，2025
- **DOI：** https://doi.org/10.1609/aaai.v39i1.32010
- **论文链接：** https://ojs.aaai.org/index.php/AAAI/article/view/32010
- **代码：** https://github.com/Xubin-s-Lab/PRAGA

## 研究问题

PRAGA 面向空间多模态组学数据的整合与空间域识别。论文指出，固定 K 近邻图可能难以充分捕捉测序点之间潜在的语义关系，同时实际数据中的空间域数量和点位类别通常并不预先确定。

## 方法概述

PRAGA 为不同组学模态学习特征图，并将其与空间邻接关系结合，构建自适应聚合图。模型通过图卷积网络提取模态特异性表示，再进行跨模态整合。其动态原型对比学习模块使用贝叶斯高斯混合模型调整聚类原型，并通过簇的分裂与合并适应潜在类别数量。整体优化结合图同质性约束、特征重构损失和动态原型对比损失。

## 证据记录

- **PRAGA2025:E01：动态图构建。** 支持 PRAGA 使用动态图捕捉潜在语义关系，并结合空间信息与特征语义。位置：摘要及引言，论文第326–327页。
- **PRAGA2025:E02：动态原型学习。** 支持模型使用贝叶斯高斯混合模型及簇分裂、合并机制调整原型数量。位置：方法部分“Dynamic Prototype Contrastive Learning”，第328–329页。
- **PRAGA2025:E03：联合优化目标。** 支持总损失由同质性、重构和动态原型对比损失构成。位置：方法部分公式（14），第329页。

## 阅读分析

PRAGA 的主要特点是同时调整图结构和聚类原型，适合用于讨论潜在语义关系与未知空间域数量问题。动态图学习和原型更新也增加了模型实现与训练流程的复杂度。后一判断属于方法分析，不应表述为论文作者明确提出的局限性。
