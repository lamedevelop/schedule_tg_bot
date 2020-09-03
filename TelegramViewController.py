from telebot import types

from DbManager import DbManager


class TelegramViewController:


    def __init__(self):
        self.dbManager = DbManager()


    def getStartMsg(self):
        return '''Hello {}!\nIt's telegram schedule bot'''


    def getStartKeyboardMarkup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        universities = self.dbManager.getUniversities()
        
        for university in universities:
            markup.row(university[0])

        return markup
