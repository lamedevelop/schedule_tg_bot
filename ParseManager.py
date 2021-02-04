import re
import ast
from datetime import datetime

from DbManager import DbManager
from Controllers.TelegramViewController import TelegramViewController
from Controllers.Parse.MpeiParseController import MpeiAbstractParseController
from Controllers.Parse.BmstuParseController import BmstuAbstractParseController


class ParseManager(object):

    def __init__(self):
        self.parse_controllers = {
            MpeiAbstractParseController.university_name: MpeiAbstractParseController(),
            BmstuAbstractParseController.university_name: BmstuAbstractParseController(),
        }

    def downloadSchedule(self, university_id: int, group_name: str) -> str:
        university_name = DbManager.getUniversity(university_id)['university_name']
        return self.parse_controllers[university_name] \
            .makeJson(group_name.upper()) \
            .replace('\'', '\"')  # here is upper

    @staticmethod
    def filterGroup(message) -> str:
        if message[-1:] == ".":
            message = message[:-1]
        return message.lower()  # and here is lower. So lower or upper?

    @staticmethod
    def getDaySchedule(day_name: str, json_schedule: str) -> str:
        numWeek = int(datetime.today().strftime("%U"))

        output_text = ['Расписание на *%s*' %
                       re.sub(r'а$', 'у', day_name.lower())]
        dict_schedule = list(ast.literal_eval(json_schedule).values())[0]
        scheduleForDay = dict_schedule[day_name]

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

            output_text.append(
                '\n'.join(list(filter(bool, nextLine))))

        activeSlots = list(filter(bool, output_text))
        if len(activeSlots) == 1:
            return '*%s* - выходной день' % day_name

        return '\n\n'.join(activeSlots)
