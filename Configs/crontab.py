crontab = {
    'tasks': [
        {
            'name': "schedule_update",
            'command': "* * * * * . /etc/profile; python3 /usr/src/app/RunManager.py --manager=Db --action=updateGroups",
            'comment': "schedule update",
            'is_active': True,
        },
        {
            'name': "dump_logs_and_db",
            'command': "* * * * * . /etc/profile; python3 /usr/src/app/RunManager.py --manager=MonitoringAlert --action=dump",
            'comment': "dump logs and db to telegram chat",
            'is_active': True,
        },
    ]
}


def getCrontab():
    return crontab
