#!/bin/bash

openssl req -newkey rsa:2048 -sha256 -nodes -keyout private.key -x509 -days 3650 -out cert.pem

mkdir Logs

python3 RunManager.py --manager=Db --action=startupDb
python3 RunManager.py --manager=Cron --action=install

echo "Update Configs/main.py before running bot"
echo "After run command"
echo ">> python3 Bot.py"