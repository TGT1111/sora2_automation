#!/usr/bin/env bash
# run_pipeline.sh — executes the full Sora 2 content preparation flow
# Stop immediately if any step fails
set -e

echo "🚀 Starting Sora 2 content pipeline..."
echo "1. Collecting raw content..."
python3 src/agents/collector.py
echo "2. Cleaning content..."
python3 src/agents/cleaner.py
echo "3. Analyzing content..."
python3 src/agents/analyzer.py
echo "4. Generating insights..."
python3 src/agents/summarizer.py
echo "✅ Pipeline complete! See analysis/insights.txt for results."
