from datetime import datetime


class DateTimeController:

    days_of_week = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье",
    }

    @staticmethod
    def getCurrDate():
        return datetime.now().strftime("%d-%m-%Y")

    @staticmethod
    def getCurrDateAndTime():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    @staticmethod
    def getCurrDayOfWeek():
        return datetime.today().weekday()
