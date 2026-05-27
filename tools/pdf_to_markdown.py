from __future__ import annotations

import argparse
import re
from pathlib import Path

from pypdf import PdfReader


def is_cjk_char(text: str) -> bool:
    return len(text) == 1 and "\u4e00" <= text <= "\u9fff"


def looks_like_code(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False

    code_starts = (
        "public ",
        "private ",
        "protected ",
        "int ",
        "long ",
        "double ",
        "float ",
        "boolean ",
        "String ",
        "for",
        "while",
        "if",
        "return ",
        "System.",
        "//",
        "/*",
        "*",
    )
    return (
        stripped.startswith(code_starts)
        or stripped in {"{", "}", "}", "};"}
        or stripped.endswith(";")
        or stripped.endswith("{")
        or stripped.endswith("}")
    )


def clean_extracted_text(text: str) -> str:
    cleaned: list[str] = []
    in_code = False
    code_indent = 0

    for raw_line in text.replace("\r\n", "\n").replace("\xa0", " ").split("\n"):
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            if in_code:
                cleaned.append("")
                continue
            if cleaned and cleaned[-1] != "":
                cleaned.append("")
            continue

        if looks_like_code(line):
            if not in_code:
                if cleaned and cleaned[-1] != "":
                    cleaned.append("")
                cleaned.append("```java")
                in_code = True
                code_indent = 0
            if stripped.startswith("}"):
                code_indent = max(0, code_indent - 1)
            cleaned.append(("    " * code_indent) + stripped)
            if stripped.endswith("{"):
                code_indent += 1
            continue

        if in_code:
            cleaned.append("```")
            in_code = False

        # Some teaching PDFs encode Chinese titles as characters separated by large spaces.
        line = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", stripped)
        line = re.sub(r"(?<=[\u4e00-\u9fff])\s{2,}(?=[A-Za-z0-9（(])", "", line)
        line = re.sub(r"(?<=[A-Za-z0-9）)])\s{2,}(?=[\u4e00-\u9fff])", "", line)
        line = re.sub(r"\s{2,}", " ", line)
        cleaned.append(line)

    if in_code:
        cleaned.append("```")

    text = "\n".join(cleaned)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff，；、])\n(?=[\u4e00-\u9fff])", "", text)
    return text.strip() + "\n"


def pdf_to_markdown(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    chunks = [f"# {pdf_path.stem}", ""]

    for index, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text(extraction_mode="layout") or ""
        page_text = clean_extracted_text(page_text)
        if page_text.strip():
            chunks.extend([f"## 第 {index} 页", "", page_text.strip(), ""])

    return "\n".join(chunks).strip() + "\n"


def iter_pdfs(input_path: Path) -> list[Path]:
    if input_path.is_file() and input_path.suffix.lower() == ".pdf":
        return [] if input_path.name.startswith("._") else [input_path]
    return sorted(
        path
        for path in input_path.rglob("*.pdf")
        if not any(part.startswith("._") for part in path.parts)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert text-based PDFs to Markdown.")
    parser.add_argument("input", type=Path, help="PDF file or directory containing PDFs")
    parser.add_argument("output", type=Path, help="Output directory for Markdown files")
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    input_root = args.input if args.input.is_dir() else args.input.parent

    for pdf_path in iter_pdfs(args.input):
        markdown = pdf_to_markdown(pdf_path)
        relative_path = pdf_path.relative_to(input_root).with_suffix(".md")
        output_path = args.output / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        print(output_path)


if __name__ == "__main__":
    main()
