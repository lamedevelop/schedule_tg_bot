from Scripts.db_interact import main
from datetime import datetime
import re
import ast

from DbManager import DbManager

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
    def updateUserSchedule() -> None:
        pass

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


if __name__ == "__main__":
    out_put = '''{"А-06М-20": {"Понедельник": {"09:20-10:55": {"both": [""]}, "11:10-12:45": {"both": [""]}, "13:45-15:20": {"both": [""]}, "15:35-17:10": {"both": [""]}, "17:20-18:55": {"both": [""]}}, "Вторник": {"09:20-10:55": {"both": ["Зачет с оценкой", "Иностранный язык", "ЭО и ДОТ", ""]}, "11:10-12:45": {"both": [""]}, "13:45-15:20": {"both": [""]}, "15:35-17:10": {"both": [""]}, "17:20-18:55": {"both": [""]}}, "Среда": {"09:20-10:55": {"both": [""]}, "11:10-12:45": {"both": [""]}, "13:45-15:20": {"both": [""]}, "15:35-17:10": {"both": [""]}, "17:20-18:55": {"both": [""]}}, "Четверг": {"09:20-10:55": {"both": ["Зачет с оценкой", "Современные проблемы информатики и вычислительной техники", "ЭО и ДОТ", "ст.преп. Коротких Т.Н."]}, "11:10-12:45": {"both": [""]}, "13:45-15:20": {"both": [""]}, "15:35-17:10": {"both": [""]}, "17:20-18:55": {"both": [""]}}, "Пятница": {"09:20-10:55": {"both": [""]}, "11:10-12:45": {"both": [""]}, "13:45-15:20": {"both": [""]}, "15:35-17:10": {"both": [""]}, "17:20-18:55": {"both": [""]}}, "Суббота": {"09:20-10:55": {"both": [""]}, "11:10-12:45": {"both": [""]}, "13:45-15:20": {"both": [""]}, "15:35-17:10": {"both": [""]}, "17:20-18:55": {"both": [""]}}}}'''
    group_name = 'а-06м-20'
    unic_id = '1'
    day_name = 'Вторник'
    res = '''Расписание на *вторник*

*09:20-10:55*
*Иностранный язык*
_Зачет с оценкой_
_ЭО и ДОТ_'''

    lol = ParseManager.getJson(unic_id, group_name)
    if lol == out_put:
        print(f'getJson: Good')

    lol = ParseManager.getDaySchedule(day_name, lol)
    if res == lol:
        print(f'getDaySchedule: Good')

    group_name = 'иу3-52б'
    unic_id = '2'
    day_name = 'Понедельник'
    res = '''Расписание на *понедельник*

*13:50-15:25*
*Основы теории управления и цифровой обработки сигналов*
_(лек)_
_533_
Недашковский В. М.

*15:40-17:15*
*Дискретная математика*
_(сем)_
_430_
Виноградова М. С.

*17:25-19:00*
*Схемотехника электронных устройств*
_(лек)_
_520_
Амурский В. Б.'''

    lol = ParseManager.getJson(unic_id, group_name)
    lol = ParseManager.getDaySchedule(day_name, lol)
    if res == lol:
        print(f'getDaySchedule: Good')
