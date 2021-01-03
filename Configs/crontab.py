crontab = {
    'tasks': [
        {
            'name': "schedule_update",
            'command': "0 1 * * 6 /usr/local/bin/python3 /usr/src/app/RunManager.py --manager=Db --action=updateGroups",
            'comment': "schedule update",
            'is_active': True,
        },
        {
            'name': "dump_logs_and_db",
            'command': "0 1 * * 6 /usr/local/bin/python3 /usr/src/app/RunManager.py --manager=MonitoringAlert --action=dump",
            'comment': "dump logs and db to telegram chat",
            'is_active': True,
        },
        {
            'name': "task3",
            'command': '* * * * * run something 3',
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
