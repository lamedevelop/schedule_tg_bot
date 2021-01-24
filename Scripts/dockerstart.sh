#!/bin/sh
# dockerstart is entry point for docker container
cd /usr/src/app

python3 RunManager.py --manager=Db --action=upAllMigrations
python3 RunManager.py --manager=Db --action=fillGroups
python3 RunManager.py --manager=Cron --action=install

crond -b
python3 Bot.py
