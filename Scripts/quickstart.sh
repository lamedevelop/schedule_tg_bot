#!/bin/bash

#openssl req -newkey rsa:2048 -sha256 -nodes -keyout private.key -x509 -days 3650 -out cert.pem

mkdir Logs

python3 RunManager.py --manager=Db --action=upAllMigrations
python3 RunManager.py --manager=Db --action=resetDb

echo "Update Configs/tgConfig.py before running bot"
