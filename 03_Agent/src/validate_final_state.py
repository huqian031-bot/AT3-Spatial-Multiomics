#!/usr/bin/env python3
"""检查研究简报结构、来源证据、DOI 与一页篇幅要求。"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source_package"
BRIEF = ROOT / "results" / "final-brief.md"

REQUIRED_HEADINGS = [
    "## 研究问题",
    "## 三种方法比较",
    "## 综合比较",
    "## 结论与启示",
    "## 参考文献",
]
REQUIRED_EVIDENCE = [
    "PRAGA2025:E01",
    "PRAGA2025:E02",
    "SPATIALGLUE2024:E01",
    "SPATIALGLUE2024:E02",
    "COSMOS2025:E01",
    "COSMOS2025:E02",
]
REQUIRED_DOIS = [
    "10.1609/aaai.v39i1.32010",
    "10.1038/s41592-024-02316-4",
    "10.1038/s41467-024-55204-y",
]
MIN_CHARS = 700
MAX_CHARS = 1800


def validate(path: Path = BRIEF) -> tuple[bool, list[str], int]:
    errors: list[str] = []
    if not path.exists():
        return False, [f"未找到简报文件：{path}"], 0

    text = path.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"缺少必要章节：{heading}")

    for evidence in REQUIRED_EVIDENCE:
        if f"[{evidence}]" not in text:
            errors.append(f"缺少正文证据引用：{evidence}")

    for doi in REQUIRED_DOIS:
        if doi not in text:
            errors.append(f"缺少参考文献 DOI：{doi}")

    for source_file in [
        "PRAGA_2025.md",
        "SpatialGlue_2024.md",
        "COSMOS_2025.md",
    ]:
        source_path = SOURCE_DIR / source_file
        if not source_path.exists():
            errors.append(f"来源文件不存在：{source_file}")
            continue
        source_text = source_path.read_text(encoding="utf-8")
        source_ids = set(re.findall(r"[A-Z]+[0-9]{4}:E[0-9]{2}", source_text))
        for cited in re.findall(r"\[([A-Z]+[0-9]{4}:E[0-9]{2})\]", text):
            if cited.startswith(source_file.split("_")[0].upper()) and cited not in source_ids:
                errors.append(f"引用编号未在来源文件中找到：{cited}")

    char_count = len(re.sub(r"\s", "", text))
    if char_count < MIN_CHARS:
        errors.append(f"简报过短：{char_count} 字符，至少需要 {MIN_CHARS}。")
    if char_count > MAX_CHARS:
        errors.append(f"简报超出一页简报长度控制：{char_count} 字符，最多 {MAX_CHARS}。")

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
