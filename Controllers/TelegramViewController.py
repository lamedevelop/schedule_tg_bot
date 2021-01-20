import json
from aiogram.types import ReplyKeyboardMarkup

from DbManager import DbManager
from AlertManager import AlertManager
from Controllers.Log.LogController import LogController
from Controllers.DateTimeController import DateTimeController
from Controllers.Translation.TranslationController import TranslationController


class TelegramViewController:
    icons = {
        "snowman": u'\U000026C4',
        "watches": u'\U0001F551',
        "look_here_left": u'\U0001F449',
        "look_here_right": u'\U0001F448'
    }

    @staticmethod
    def getUniversityKeyboardMarkup():
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        universities = DbManager.getUniversities()

        if not universities:
            LogController().alert("getUniversityKeyboardMarkup failed: universities empty")
            AlertManager().notify(
                "getUniversityKeyboardMarkup failed: universities empty",
                AlertManager.WARNING_LEVEL
            )
            universities = [['Default']]

        for university in universities:
            markup.row(university['university_name'])

        return markup

    # old method
    # probably should be removed
    # @staticmethod
    # def getGroupKeyboardMarkup(universityId):
    #     markup = ReplyKeyboardMarkup(resize_keyboard=True)
    #     groups = DbManager().getGroupsByUniversityId(universityId)
    #
    #     for group in groups:
    #         markup.row(group[1])
    #
    #     return markup

    @staticmethod
    def removeKeyboardMarkup():
        removeKeyboard = {'remove_keyboard': True}
        removeKeyboardEncoded = json.dumps(removeKeyboard)
        return removeKeyboardEncoded

    # experimental method
    # will be updated or removed later
    # @staticmethod
    # def inlineGroupChooseKeyboardMarkup():
    #     keyboard = [["hello"], ["world"]]
    #     markup = InlineKeyboardMarkup()
    #
    #     stringList = {"Name": "John", "Language": "Python", "API": "pyTelegramBotAPI"}
    #
    #     for key, value in stringList.items():
    #         markup.add(
    #             InlineKeyboardButton(
    #                 text=value,
    #                 callback_data="['value', '" + value + "', '" + key + "']"
    #             ),
    #             InlineKeyboardButton(
    #                 text="X",
    #                 callback_data="['key', '" + key + "']"
    #             )
    #         )
    #
    #     return markup

    @staticmethod
    def getScheduleKeyboardMarkup(lang):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)

        days_of_week = TranslationController().getMessage(
            lang,
            TranslationController.WEEK_DAYS
        ).copy()

        for i in range(0, len(days_of_week)):
            days_of_week[i] = TelegramViewController.removeFilters(days_of_week[i])

        day_id = DateTimeController.getCurrDayOfWeek()
        days_of_week[day_id] = TelegramViewController.applyLookHereFilter(days_of_week[day_id])

        keyboard = [
            [days_of_week[0], days_of_week[1]],
            [days_of_week[2], days_of_week[3]],
            [days_of_week[4], days_of_week[5]]
        ]

        for keys in keyboard:
            markup.row(keys[0], keys[1])

        return markup

    @staticmethod
    def isDayOfWeek(day):
        return day in DateTimeController.days_of_week.values()

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

    @staticmethod
    def applyLookHereFilter(word):
        if TelegramViewController.icons["look_here_left"] in word \
                or TelegramViewController.icons["look_here_right"] in word:
            return word
        else:
            return TelegramViewController.icons["look_here_left"] \
                   + word \
                   + TelegramViewController.icons["look_here_right"]

    @staticmethod
    def removeFilters(word):
        day = word.title()

        for key in DateTimeController.days_of_week:
            if day == DateTimeController.days_of_week_eng[key]:
                day = DateTimeController.days_of_week[key]

        if TelegramViewController.icons["look_here_left"] in word \
                or TelegramViewController.icons["look_here_right"] in word:
            day = word.split(TelegramViewController.icons["look_here_left"])[1]
            day = day.split(TelegramViewController.icons["look_here_right"])[0]

        return day
