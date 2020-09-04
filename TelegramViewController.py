from telebot import types

from DbManager import DbManager


class TelegramViewController:

    def getStartMsg(self):
        return 'Hello {}!\n' \
               'It\'s telegram schedule bot\n' \
               'Choose your *university*'

    def getUniversitySpecifiedMsg(self):
        return "University *successfully specified*\n" \
               "Chose your *group*"

    def getGroupSpecifiedMsg(self):
        return "Group *successfully specified*\n" \
               "Here is your *schedule*"

    def getUniversityKeyboardMarkup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        universities = DbManager().getUniversities()

        for university in universities:
            markup.row(university[0])

        return markup
