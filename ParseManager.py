from Scripts.db_interact import main
from datetime import datetime
import re
import ast

from Controllers.View.TelegramViewController import TelegramViewController

from Controllers.Parse.ParseController import ParseController
from Controllers.Parse.MpeiParseController import MpeiParseController
from Controllers.Parse.BmstuParseController import BmstuParseController


class ParseManager(object):

    parse_controllers = {
        str(parse_controller()): parse_controller()
        for parse_controller in ParseController.__subclasses__()
    }

    @staticmethod
    def downloadSchedule(university_id: int, group_name: str) -> str:
        return ParseManager.parse_controllers[str(university_id)] \
                           .makeJson(group_name.upper()) \
                           .replace('\'', '\"')

    @staticmethod
    def filterGroup(message) -> str:
        if message[-1:] == ".":
            message = message[:-1]
        return message.lower()

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