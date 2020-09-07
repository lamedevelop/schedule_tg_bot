from Controllers.Parse.MpeiParseController import MpeiParseController
from Controllers.Parse.BmstuParseController import BmstuParseController

from datetime import datetime
import ast
import re


class ParseManager(object):
    # let you choose concrete parse controller and provide base interface for parsing
    comboBox = {}

    def __init__(self):
        self.comboBox[str(MpeiParseController())] = MpeiParseController()
        self.comboBox[str(BmstuParseController())] = BmstuParseController()

    def getJson(self, universityId, groupName):
        return self.comboBox[str(universityId)].makeJson(groupName.upper()).replace('\'', '\"')

    def getDaySchedule(self, dayName, jsonSchedule):

        DaysName = {
            'monday': 'Понедельник', 'tuesday': 'Вторник',
            'wednesday': 'Среда', 'thursday': 'Четверг',
            'friday': 'Пятница', 'saturday': 'Суббота'
        }

        numWeek = int(datetime.today().strftime("%U"))

        outputText = ['Расписание на %s' %
                      re.sub(r'а$', 'у', DaysName[dayName].lower())]
        jsonToDict = list(ast.literal_eval(jsonSchedule[0][0]).values())[0]
        scheduleForDay = jsonToDict[DaysName[dayName]]

        for time, scheduleArr in scheduleForDay.items():
            nextLine = []
            for scheduleType, schedule in scheduleArr.items():
                if len(schedule) > 1:
                    params = [schedule[1], time, schedule[2],
                              schedule[3], schedule[0]]
                    if scheduleType == 'both':
                        nextLine.extend(params)
                    elif numWeek % 2 == 0 and scheduleType == 'denominator':
                        nextLine.extend(params)
                        break
                    elif numWeek % 2 != 0 and scheduleType == 'numerator':
                        nextLine.extend(params)
                        break

            outputText.append(
                '\n'.join(list(filter(lambda x: bool(x), nextLine))))

        activeSlots = list(filter(lambda x: bool(x), outputText))
        if len(activeSlots) == 1:
            return '%s - выходной день' % DaysName[dayName]

        return '\n\n'.join(activeSlots)
