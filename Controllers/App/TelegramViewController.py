import json
from telebot import types

from DbManager import DbManager


class TelegramViewController:

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
    def getScheduleKeyboardMarkup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        daysOfWeek = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday"
        ]

        for day in daysOfWeek:
            markup.row(day)

        return markup
