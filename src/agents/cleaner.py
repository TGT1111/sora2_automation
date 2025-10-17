#!/usr/bin/env python3
"""
cleaner.py – preprocesses content for Sora 2 automation.
Takes files from ./clean_content/, removes filler words and odd characters,
normalizes case, and outputs to ./processed_content/.
"""

import re
from pathlib import Path

INPUT_DIR = Path("clean_content")
OUTPUT_DIR = Path("processed_content")

# simple filler list; extend as needed
FILLERS = ["uh", "um", "er", "ah", "like", "you know"]

def clean_text(text: str) -> str:
    # remove timestamps like [00:32], (12:45)
    text = re.sub(r"[\(\[]?\d{1,2}:\d{2}[\)\]]?", "", text)
    # strip filler words
    for word in FILLERS:
        text = re.sub(rf"\b{word}\b", "", text, flags=re.IGNORECASE)
    # remove extra spaces and normalize case
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

def process_files():
    OUTPUT_DIR.mkdir(exist_ok=True)
    count = 0

    for file in INPUT_DIR.glob("*"):
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8", errors="ignore")
        cleaned = clean_text(text)
        (OUTPUT_DIR / file.name).write_text(cleaned, encoding="utf-8")
        count += 1

    print(f"Processed {count} files. Output saved to {OUTPUT_DIR}/")

if __name__ == "__main__":
    process_files()
