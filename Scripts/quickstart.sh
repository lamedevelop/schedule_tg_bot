#!/bin/bash

openssl req -newkey rsa:2048 -sha256 -nodes -keyout private.key -x509 -days 3650 -out cert.pem

mkdir Logs

export $(grep -v '^#' .env | xargs)
rm -f .env

until mysql -h $MARIA_HOST -p$MARIA_PASSWORD; do
    >&2 echo "mariadb is unavailable - sleeping"
    sleep 5
done
>&2 echo "mariadb is up - executing commands"

python3 RunManager.py --manager=Db --action=upAllMigrations
python3 RunManager.py --manager=Db --action=resetDb
python3 RunManager.py --manager=Cron --action=install

echo "Update Configs/main.py before running bot"
python Bot.py