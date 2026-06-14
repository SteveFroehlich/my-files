#!/bin/bash
set -e

# sort non-hidden directories and files by their binary size
# note this also handles the case where a folder name has a dot. eg: steve.fro/ vs just leading dot, eg: .env, .git/
du -ah . | grep -v -E '/\.[^/]+($|/)' | sort -h
