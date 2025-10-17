#!/usr/bin/env python3
"""
summarizer.py – generates human-readable insights from analysis/summary.csv
Outputs recommendations highlighting readability and sentiment pain points.
"""

import csv
from pathlib import Path

INPUT_FILE = Path("analysis/summary.csv")
OUTPUT_FILE = Path("analysis/insights.txt")

def interpret_readability(score: float) -> str:
    if score <= 6:
        return "Easy to read; accessible for general users."
    elif score <= 10:
        return "Moderate complexity; consider simplifying language."
    else:
        return "Difficult text; rewrite with shorter sentences and simpler words."

def interpret_sentiment(score: float) -> str:
    if score > 0.3:
        return "Tone is positive; conveys helpful or friendly language."
    elif score < -0.3:
        return "Tone is negative; review for frustration or unclear guidance."
    else:
        return "Tone is neutral; acceptable but could be more engaging."

def summarize():
    if not INPUT_FILE.exists():
        print(f"No analysis file found at {INPUT_FILE}")
        return

    with INPUT_FILE.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        lines = list(reader)

    with OUTPUT_FILE.open("w", encoding="utf-8") as out:
        out.write("=== Content Insights Report ===\n\n")
        for row in lines:
            file = row["file"]
            try:
                readability = float(row["readability"])
                sentiment = float(row["sentiment"])
            except ValueError:
                continue
            out.write(f"File: {file}\n")
            out.write(f"  - {interpret_readability(readability)}\n")
            out.write(f"  - {interpret_sentiment(sentiment)}\n\n")

    print(f"Insights generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    summarize()
