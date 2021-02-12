#!/bin/sh

# dockerstart is entry point for docker container

#cd $PROJECT_PATH
#
#until mysql -h $MARIA_HOST -u$MYSQL_USER -p$MARIA_PASSWORD; do
#    >&2 echo "mariadb is unavailable - sleeping"
#    sleep 5
#done
#>&2 echo "mariadb is up - executing commands"

python3 RunManager.py --manager=Db --action=upAllMigrations
python3 RunManager.py --manager=Db --action=fillGroups
python3 RunManager.py --manager=Cron --action=install

crond -b
python3 Bot.py