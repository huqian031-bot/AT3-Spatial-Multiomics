# AT3：空间转录组与空间多组学方法研究

本仓库整理本次 AT3 作业中的文献综述、文献矩阵及 PRAGA 技术复现材料。

## 项目内容

- `文献综述/AT3_文献综述与PRAGA技术复现_修改版.docx`：文献综述与 PRAGA 技术复现报告。
- `文献综述/AT3_Spatial_Omics_Literature_Matrix_修改版.xlsx`：核心文献、补充文献、技术分类及 PRAGA 复现设置。
- `PRAGA复现/AT3_PRAGA_Kaggle_Reproduction.ipynb`：PRAGA 官方流程复现 Notebook。
- `PRAGA复现/PRAGA_HLN.png`：Human Lymph Node RNA+ADT 聚类可视化。
- `PRAGA复现/PRAGA_HLN.txt`：3,484 个 spot 的预测聚类标签。
- `PRAGA复现/PRAGA_HLN_train.log`：训练及聚类读出日志。
- `PRAGA复现/official_metrics.txt`：官方评价脚本输出。
- `PRAGA复现/provenance.json`：代码版本、数据校验值、运行环境、参数和评价指标记录。

## 复现实验设置

- 方法：PRAGA
- 数据：Human Lymph Node（RNA+ADT）
- 数据来源：Zenodo record 14591305
- 官方代码 commit：`4adb11c96fc7ddad800fa1787eadcc8b91b42784`
- 参数：`data_type=10x`、`n_clusters=10`、`init_k=10`、`KNN_k=20`、`RNA_weight=5`、`ADT_weight=5`
- 训练轮数：30 epochs
- 训练随机种子：2024
- mclust 聚类读出随机种子：2020，模型为 EEE

## 运行环境

本次运行记录的环境为 Python 3.13.16、PyTorch 2.11.0+cu130、AnnData 0.13.4、R mclust 6.1。Kaggle 环境检测到两张 Tesla T4，训练日志显示模型运行在 `cuda:1`。

运行 Notebook 前，在 Kaggle 中启用 GPU 和 Internet。Notebook 会克隆 PRAGA 官方仓库、下载并校验 Zenodo 数据，再执行官方 HLN 10x 流程。R 包 `mclust` 需在 R 环境中安装，不能通过 Python 的 pip requirements 完成安装。

## 本次结果

本次运行完成 30 轮训练并输出 10 个聚类。ARI 为 **0.260940**，NMI 为 **0.370346**。PRAGA 主进程总耗时约 127.46 秒，其中模型训练阶段约 29.15 秒。

本次结果与论文报告值存在差异，因此报告中将其表述为官方流程的技术复现，不表述为数值完全复现。
