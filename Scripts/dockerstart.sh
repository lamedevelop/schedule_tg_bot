#!/bin/bash

cd /Users/my_app

# cron
# cp /etc/crontab /etc/cron.d/crontab
# touch /etc/crontab /etc/cron.*/*
#chmod 0666 /etc/crontab
# crontab -u root /etc/crontab

service cron start

python3 RunManager.py --manager=Cron --action=install
python3 RunManager.py --manager=Cron --action=enable

service cron status
echo ""
crontab -l
echo ""

python3 Bot.py