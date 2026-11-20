#!/usr/bin/env bash
# Read-only environment check. Prints versions. Installs nothing.
for c in node git ffmpeg ffprobe python3 python claude codex; do
  if command -v "$c" >/dev/null 2>&1; then
    v=$("$c" --version 2>&1 | head -1)
    echo "OK      $c  $v"
  else
    echo "MISSING $c"
  fi
done
