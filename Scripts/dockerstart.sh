#!/bin/sh

# dockerstart is entry point for docker container

# shellcheck disable=SC2164
cd $1

python3 RunManager.py --manager=Db --action=startupDb
python3 RunManager.py --manager=Cron --action=install

crond -b
python3 Bot.py