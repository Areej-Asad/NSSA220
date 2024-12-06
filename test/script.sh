# Write a Bash script that takes a "linux command" as input, executes it, 
# and prints "success" if the command completes successfully or "fail" if the 
# command fails. The command should be passed as an input argument. Assuming the 
# name of the script is script.sh, see the below example runs. 
# $ bash script.sh ls 
# success 
# $ bash script.sh echo "hello" 
# success 
# $ bash script.sh cdd 
# fail

#!/bin/bash

# Check if a command is provided as input
if [ $# -lt 1 ]; then
    echo "Error: No command provided."
    echo "Usage: $0 <command>"
    exit 1
fi

# Execute the command passed as input
"$@"

# Check the exit status of the command
if [ $? -eq 0 ]; then
    echo "success"
else
    echo "fail"
fi
