import telebot
from telebot import types

from DbManager import DbManager


class TelegramViewController:


    def __init__(self):
        self.dbManager = DbManager()


    def getStartMsg(self):
        return '''Hello {}!\nIt's schedule bot'''


    def getStartKeyboardMarkup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        universities = self.dbManager.getUniversities()
        
        for universitiy in universities:
            markup.row(universitiy)

        return markup
