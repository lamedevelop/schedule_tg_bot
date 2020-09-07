from datetime import datetime


class DateTimeController:

    @staticmethod
    def getCurrDate():
        return datetime.now().strftime("%d-%m-%Y")

    @staticmethod
    def getCurrDateAndTime():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")