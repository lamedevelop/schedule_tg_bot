crontab = {
    'tasks': [
        {
            'name': "task1",
            'command': "* * * * * run something 1",
            'comment': "task 1",
            'is_active': True,
        },
        {
            'name': "task2",
            'command': "* * * * * run something 2",
            'comment': "task 2",
            'is_active': False,
        },
        {
            'name': "task3",
            'command': "* * * * * run something 3",
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
