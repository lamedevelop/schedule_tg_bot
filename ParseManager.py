import re
import ast
from datetime import datetime

from Controllers.View.TelegramViewController import TelegramViewController
from Controllers.Parse.ParseController import *


class ParseManager(object):

    def __init__(self):
        subs = ParseController.__subclasses__()
        self.comboBox = {str(obj()): obj() for obj in subs}

    def getJson(self, universityId, groupName):
        return self.comboBox[str(universityId)].makeJson(groupName.upper()).replace('\'', '\"')

    def getDaySchedule(self, dayName, jsonSchedule):
        numWeek = int(datetime.today().strftime("%U"))

        outputText = ['Расписание на *%s*' %
                      re.sub(r'а$', 'у', dayName.lower())]
        jsonToDict = list(ast.literal_eval(jsonSchedule[0][0]).values())[0]
        scheduleForDay = jsonToDict[dayName]

        for time, scheduleArr in scheduleForDay.items():
            nextLine = []
            for scheduleType, schedule in scheduleArr.items():
                if len(schedule) > 1:
                    params = [
                        time,
                        schedule[1],
                        schedule[2],
                        schedule[3],
                        schedule[0]
                    ]

                    params = TelegramViewController.applyMarkup(params)

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
            return '*%s* - выходной день' % dayName

        return '\n\n'.join(activeSlots)

    def filterGroup(self, message, university_id):
        if message[-1:] == ".":
            message = message[:-1]

        return message.lower()
