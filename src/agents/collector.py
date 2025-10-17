#!/usr/bin/env python3
"""
collector.py – gathers and normalizes raw content for the Sora 2 automation pipeline.
Scans ./raw_content for .txt or .csv files, copies them into ./clean_content/,
and logs a summary report.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

RAW_DIR = Path("raw_content")
CLEAN_DIR = Path("clean_content")
LOG_FILE = Path("analysis/collector_log.txt")

def collect_files():
    CLEAN_DIR.mkdir(exist_ok=True)
    LOG_FILE.parent.mkdir(exist_ok=True)
    collected = []

    for file in RAW_DIR.glob("*"):
        if file.suffix.lower() in [".txt", ".csv"]:
            destination = CLEAN_DIR / file.name
            shutil.copy(file, destination)
            collected.append(file.name)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] Collected {len(collected)} files:\n")
        for name in collected:
            log.write(f" - {name}\n")
        log.write("\n")

    print(f"Collected {len(collected)} files. See {LOG_FILE} for details.")

if __name__ == "__main__":
    collect_files()
