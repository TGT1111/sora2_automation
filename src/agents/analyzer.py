#!/usr/bin/env python3
"""
analyzer.py – analyzes cleaned content for readability and sentiment.
Reads ./processed_content/, computes metrics, and writes analysis/summary.csv.
"""

import csv
from pathlib import Path
import textstat
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon", quiet=True)

INPUT_DIR = Path("processed_content")
OUTPUT_DIR = Path("analysis")
OUTPUT_FILE = OUTPUT_DIR / "summary.csv"

def analyze_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        return {
            "file": path.name,
            "word_count": 0,
            "readability": 0.0,
            "sentiment": 0.0,
        }

    readability = round(textstat.flesch_kincaid_grade(text), 2)
    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)["compound"]
    word_count = len(text.split())

    return {
        "file": path.name,
        "word_count": word_count,
        "readability": readability,
        "sentiment": round(sentiment, 3),
    }

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    results = [analyze_file(p) for p in INPUT_DIR.glob("*") if p.is_file()]

    if not results:
        print("No files to analyze.")
        return

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"Analysis complete. Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
