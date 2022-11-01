#!/bin/bash

## please execute the script under base environment
## execute this file with command 'bash multiVersionTest.sh'

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

arguments=$@
set -- "${@:5}"   # Configure arguments
source activate
set -- "${arguments[@]}"  # Restore arguments

envs=("python36" "python37" "python38" "python39" "python310")

for env in "${envs[@]}"; do
    conda activate $env
    python --version 
    python $SCRIPT_DIR/fullTest.py $arguments
done