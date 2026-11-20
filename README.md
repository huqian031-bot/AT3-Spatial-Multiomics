# AT3：深度学习在空间转录组与空间多组学整合中的方法研究

本仓库对应 AT3 累积式大作业，包含文献综述、PRAGA 技术复现和 Agent 工作任务三部分。

GitHub 仓库：https://github.com/huqian031-bot/AT3-Spatial-Multiomics

## 项目目录

```text
AT3-Spatial-Multiomics/
├── README.md
├── 01_Literature_Review/
│   ├── AT3_文献综述与PRAGA技术复现.docx
│   └── AT3_Spatial_Omics_Literature_Matrix.xlsx
├── 02_PRAGA_Reproduction/
│   ├── AT3_PRAGA_Kaggle_Reproduction.ipynb
│   ├── requirements.txt
│   ├── PRAGA_HLN.png
│   ├── PRAGA_HLN.txt
│   ├── PRAGA_HLN_train.log
│   ├── official_metrics.txt
│   └── provenance.json
└── 03_Agent/
    ├── README.md
    ├── source_package/
    │   ├── PRAGA_2025.md
    │   ├── SpatialGlue_2024.md
    │   └── COSMOS_2025.md
    ├── src/
    │   ├── run_agent.py
    │   └── validate_final_state.py
    └── results/
        ├── final-brief.md
        ├── task-contract.json
        ├── tool-schema.json
        ├── trajectory.jsonl
        ├── tool-results.jsonl
        ├── evaluation.csv
        ├── error-note.md
        ├── experiment-analysis.md
        └── provenance.json
```

## ① 文献综述

文献综述报告和 Excel 文献矩阵位于 `01_Literature_Review/`。报告包含研究范围、核心论文、技术知识图谱、比较分析、一页摘要及参考文献。

## ② PRAGA 技术复现

复现对象为 PRAGA（AAAI 2025），数据为 Human Lymph Node RNA+ADT。Notebook、聚类图、预测标签、训练日志、官方指标输出和 provenance 位于 `02_PRAGA_Reproduction/`。

本次保存的运行结果：30 epochs，10 个聚类，ARI = 0.260940，NMI = 0.370346。训练日志记录的模型训练时间约 29.15 秒，主进程总耗时约 127.46 秒。该结果与论文报告值存在差异，报告中按实际结果说明，不表述为数值完全复现。

### 运行方式

1. 在 Kaggle 中打开 `AT3_PRAGA_Kaggle_Reproduction.ipynb`。
2. 开启 GPU 和 Internet。
3. 按顺序运行 Notebook 单元。环境配置部分会安装 Python 依赖并将 R 包 mclust 固定为 6.1。
4. Notebook 会克隆 PRAGA 官方仓库、下载 Zenodo 数据并校验 MD5，再运行 Human Lymph Node 10x 流程。

Python 依赖见 `02_PRAGA_Reproduction/requirements.txt`。PyTorch 使用 Kaggle GPU 镜像预装版本；R 和 mclust 由 Notebook 的环境配置单元处理。

## ③ Agent 工作任务

Agent 使用 **Python 本地工具调用 Agent（规则驱动流程）**，完成离线来源检索、三篇资料读取、方法比较、简报生成和 final-state validator 校验。该流程不调用外部模型 API，不需要 GPU 或网络。

在 `03_Agent/` 目录运行：

```bash
python src/run_agent.py
python src/validate_final_state.py
```

受控比较只改变 `max_steps`（3 与 6），其余任务、来源、工具定义和校验规则保持一致。完整调用轨迹、工具返回、评价结果和运行来源记录均保存在 `03_Agent/results/`。

## 提交提示

课程平台按教师要求提交文献综述报告、文献矩阵、PRAGA 结果说明、Agent 一页简报和不超过两页的实验分析；同时在提交说明中附上本仓库链接。
