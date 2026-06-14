#!/bin/bash
set -e

# Finds all non-hidden files, gets human-readable sizes, and sorts them
find . -type f -not -path '*/.*' -exec du -h {} + | sort -h


