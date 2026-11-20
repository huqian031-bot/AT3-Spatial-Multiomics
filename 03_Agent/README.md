# AT3 Agent：空间多组学文献整理

## 任务目标

从本地离线来源包中检索并读取 PRAGA、SpatialGlue 和 COSMOS 三篇论文的结构化资料，比较方法设计，生成带正文证据编号和参考文献 DOI 的中文研究简报，并运行 final-state validator。

## 使用的 Agent

本部分使用 **Python 本地工具调用 Agent（规则驱动流程）**。Agent 通过 `search_sources`、`read_source`、`synthesize_brief` 和 `write_brief` 四类工具完成任务，不调用外部模型 API，不需要 GPU 或网络。

简报中的方法描述来自 Agent 实际读取的 `source_package/` 文件；生成过程会提取“研究问题”“方法概述”“阅读分析”和“证据记录”章节，不将论文方法正文预先写死在生成函数中。

## 目录说明

- `source_package/`：三篇论文的离线结构化阅读资料。
- `src/run_agent.py`：Agent 工具调用流程、受控比较及过程记录生成。
- `src/validate_final_state.py`：最终简报校验器。
- `results/final-brief.md`：一页研究简报。
- `results/task-contract.json`：任务定义和完成标准。
- `results/tool-schema.json`：工具定义。
- `results/trajectory.jsonl`：工具调用轨迹。
- `results/tool-results.jsonl`：工具返回内容及读取证据。
- `results/evaluation.csv`：受控比较结果。
- `results/error-note.md`：失败情况和错误记录。
- `results/experiment-analysis.md`：两页以内的实验分析。
- `results/provenance.json`：运行环境、来源文件哈希和实验结果。

## 运行方法

在 `03_Agent/` 目录下运行：

```bash
python src/run_agent.py
python src/validate_final_state.py
```

仅使用 Python 标准库，无需安装额外 Python 包。运行后会重新生成 `results/` 中的实验记录和简报。

## 受控比较

比较 `max_steps=3` 与 `max_steps=6`。两组使用相同任务、来源文件、工具定义和 validator，只改变最大工具调用步数。三步组因步骤预算不足而未完成；六步组完成三篇来源读取、简报生成和最终状态校验。

## 结果说明

`results/` 中保留了本次运行产生的轨迹、工具观察、评价、错误记录和 provenance。该 Agent 是本地规则驱动的工具调用流程，不将其描述为调用了外部大语言模型。
