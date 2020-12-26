ENTER_UNIVERSITY = 'Hello *{}*!\nCurrently we support only 2 russian universities.' \
                   'But we glad to see you here. You can continue now and check this bot functionality.\n' \
                   'Choose your *university*'

FIRST_ENTER_GROUP = 'University *chosen*\n' \
                    'Enter your group number, *in russian language*\n' \
                    'Example: *а-12м-20* in case МЭИ' \
                    'or *иу3-13б* in case МГТУ'

CHANGE_GROUP = 'Enter new *group* in russian language\n' \
               'Example: *а-12м-20* or *иу3-13б*'

SCHEDULE_WAS_FOUND = "Group was *found*!\nChose day to see your *schedule*"

SCHEDULE_DOWNLOADED = "Schedule was *downloaded*!\n" \
                      "Choose day to see your *schedule*"

SCHEDULE_WAS_NOT_FOUND = "Group *was not found*!\nTry another group"

HELP = '''
Start of using
/start

Change your *university* and *group*
/changeuniversity

Change *group* in your current university
/changegroup

Get this message
/help

Number of group should be entered in *russian language*. Example:
ИУ3-13б
А-12м-20

Dev team contacts:
@kekmarakek и @grit4in
'''

WEEK_DAYS = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}

WEEK_DAYS_SHORT = {
    1: 'Mo',
    2: 'Tu',
    3: 'We',
    4: 'Th',
    5: 'Fr',
    6: 'Sa',
    7: 'Su',
}