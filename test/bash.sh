# review bash
# Using sampledata.txt file, write bash script calculates sum 
# of sales (3rd column) for all lines starting with letters from A-F. 
# Name  script sum.sh

$ bash sum.sh sampledata.txt
41

#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 filename"
    exit 1
fi
awk '/^[A-Fa-f]/ {sum += $3} END {print sum}' "$1"
