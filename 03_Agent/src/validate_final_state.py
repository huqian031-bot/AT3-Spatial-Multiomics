#!/usr/bin/env python3
"""检查中文研究简报的结构、来源引用和参考文献信息。"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BRIEF = ROOT / "results" / "final-brief.md"
REQUIRED_HEADINGS = ["## 研究问题", "## 三种方法比较", "## 综合比较", "## 结论与启示", "## 参考文献"]
REQUIRED_EVIDENCE = ["PRAGA2025:E01", "SPATIALGLUE2024:E01", "COSMOS2025:E01"]
REQUIRED_DOIS = ["10.1609/aaai.v39i1.32010", "10.1038/s41592-024-02316-4", "10.1038/s41467-024-55204-y"]


def validate(path: Path = BRIEF) -> tuple[bool, list[str], int]:
    errors: list[str] = []
    if not path.exists():
        return False, [f"未找到简报文件：{path}"], 0
    text = path.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"缺少必要章节：{heading}")
    for evidence in REQUIRED_EVIDENCE:
        if evidence not in text:
            errors.append(f"缺少来源证据编号：{evidence}")
    for doi in REQUIRED_DOIS:
        if doi not in text:
            errors.append(f"缺少参考文献 DOI：{doi}")
    if len(text) < 300:
        errors.append("简报内容过短，请检查生成结果。")
    char_count = len(re.sub(r"\s", "", text))
    return not errors, errors, char_count


if __name__ == "__main__":
    ok, errors, char_count = validate()
    print(f"简报字符数（不含空白）：{char_count}")
    if ok:
        print("最终状态校验：通过")
        sys.exit(0)
    print("最终状态校验：未通过")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
