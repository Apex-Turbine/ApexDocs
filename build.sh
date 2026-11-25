#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-all}"
FORMAT="${2:-both}"
OUTPUT="${3:-dist}"

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  PYTHON_BIN="python"
fi

"$PYTHON_BIN" build_docs.py --target "$TARGET" --format "$FORMAT" --output "$OUTPUT"
