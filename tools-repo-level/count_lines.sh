#!/bin/bash

# Ensure the script exits if a command fails
set -e

#  Run find, count lines, ignore dotfiles, and sort numerically
#
#  it runs from the directory the script is called from. See usage.
#  usge: 
#       tools-repo-level/count_lines.sh
#
find . -type f -not -path '*/.*' -exec wc -l {} + | sort -n


