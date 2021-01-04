#!/bin/bash
# dockerstart is entry point for docker container
cd /usr/src/app

python3 RunManager.py --manager=Cron --action=install

echo ">> service cron start"
service cron start
echo ">> service cron status"
service cron status
echo ">> crontab -l"
crontab -l
echo

python3 Bot.py