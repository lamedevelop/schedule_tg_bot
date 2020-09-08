import json
from telebot import types

import telegram

from DbManager import DbManager


class TelegramViewController:

    icons = {
        "snowman": u'\U000026C4',
        "watches": u'\U0001F551'
    }

    @staticmethod
    def getUniversityKeyboardMarkup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        universities = DbManager().getUniversities()

        for university in universities:
            markup.row(university[0])

        return markup

    # old method
    # probably should be removed
    @staticmethod
    def getGroupKeyboardMarkup(universityId):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        groups = DbManager().getGroupsByUniversityId(universityId)

        for group in groups:
            markup.row(group[1])

        return markup

    @staticmethod
    def removeKeyboardMarkup():
        removeKeyboard = {'remove_keyboard': True}
        removeKeyboardEncoded = json.dumps(removeKeyboard)
        return removeKeyboardEncoded

    @staticmethod
    def inlineGroupChooseKeyboardMarkup():
        keyboard = [["hello"], ["world"]]
        markup = types.InlineKeyboardMarkup()

        stringList = {"Name": "John", "Language": "Python", "API": "pyTelegramBotAPI"}

        for key, value in stringList.items():
            markup.add(
                types.InlineKeyboardButton(
                    text=value,
                    callback_data="['value', '" + value + "', '" + key + "']"
                ),
                types.InlineKeyboardButton(
                    text="X",
                    callback_data="['key', '" + key + "']"
                )
            )

        return markup

    @staticmethod
    def getScheduleKeyboardMarkup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        daysOfWeek = [
            ["Понедельник", "Вторник"],
            ["Среда", "Четверг"],
            ["Пятница", "Суббота"]
        ]

        for day in daysOfWeek:
            markup.row(day[0], day[1])

        return markup

    @staticmethod
    def applyMarkup(params: list):

        watches = TelegramViewController.icons.get('watches')

        result = [
            # watches + " *" + params[0] + "*",       # time
            "*" + params[0] + "*",     # time
            "*" + params[1] + "*",     # lesson name
            "_" + params[4] + "_",     # type of lesson
            "_" + params[2] + "_",     # room
            params[3]                  # teacher name
        ]

        return result
