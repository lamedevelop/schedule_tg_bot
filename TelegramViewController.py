from telebot import types

from DbManager import DbManager


class TelegramViewController:

    def getStartMsg(self):
        return 'Hello {}!\n' \
               'It\'s telegram schedule bot'

    def getChooseYourUniversityMsg(self):
        return "Choose your *university*"

    def getUniversitySpecifiedMsg(self):
        return "University *successfully specified*"

    def getChooseYourGroupMsg(self):
        return "Choose your *group*"

    def getGroupSpecifiedMsg(self):
        return "Group *successfully specified*\n" \
               "Here is your *schedule*"

    def getUniversitySetMarkup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("/setuniversity")

        return markup

    def getUniversityKeyboardMarkup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        universities = DbManager().getUniversities()

        for university in universities:
            markup.row(university[0])

        return markup

    def getGroupSetMarkup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("/setgroup")

        return markup

    def getGroupKeyboardMarkup(self, universityId):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        groups = DbManager().getGroupsByUniversityId(universityId)

        for group in groups:
            markup.row(group[1])

        return markup

    def getScheduleKeyboardMarkup(self):
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

        print("getScheduleKeyboardMarkup finished")

        return markup
