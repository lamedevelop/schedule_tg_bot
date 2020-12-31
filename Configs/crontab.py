crontab = {
    'tasks': [
        {
            'name': "schedule_update",
            'command': "* * * * * /usr/local/bin/python3 /usr/src/app/RunManager.py --manager=Db --action=updateGroups >> /tmp/updateGroups.log",
            'comment': "schedule update",
            'is_active': True,
        },
        {
            'name': "dump_logs_and_db",
            'command': "* * * * * cd /usr/src/app;now=dump_$(date +'%d-%m-%Y').tar.bz2;/bin/tar -czf ${now} Logs/* sqlite.db;/usr/bin/curl -F document=@\"${now}\" https://api.telegram.org/bot<token>/sendDocument?chat_id=<chat_id> >> /tmp/2.log",
            'comment': "dump logs and db to telegram chat",
            'is_active': False,
        },
        {
            'name': "task3",
            'command': "* * * * * echo now=\"dump_$(date + \"%d-%m-%Y\").tar.bz2\" >> /tmp/3.log",
            'comment': "task 3",
            'is_active': False,
        },
        {
            'name': "task4",
            'command': "* * * * * run something 4",
            'comment': "task 4",
            'is_active': False,
        },
    ]
}


def getCrontab():
    return crontab
