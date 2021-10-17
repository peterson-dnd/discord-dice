#!/usr/bin/env bash

ROOT_PATH=$(realpath $0)
echo $ROOT_PATH
cd $ROOT_PATH

if [ "$?" ne "0" ]; then
    echo -e "Failed to cd to root path. ${ROOT_PATH}"
    exit 1
fi

# Get latest git updates
git checkout main
git pull

# Activate Venv
source bin/activate

# Update Venv
python -m pip install -r requirements.txt

# Stop App
OLD_PROCESS_ID="$(ps -ef | grep $(whoami) | grep -v 'grep' | grep 'python' | cut -d ' ' -f7-8)"

if [ ! -z $OLD_PROCESS_ID ]; then
    kill -15 $OLD_PROCESS_ID
    sleep 10
fi

# Run App
python3 ./main.py 


