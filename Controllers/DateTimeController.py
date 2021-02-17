from time import sleep
from datetime import datetime, timedelta
import Controllers.Translation.MessagesTranslation.ru as ru
import Controllers.Translation.MessagesTranslation.en as en


class DateTimeController:

    days_of_week = ru.WEEK_DAYS
    days_of_week_eng = en.WEEK_DAYS

    @staticmethod
    def getCurrDate() -> str:
        """Get date for logs filenames.

        @note This format required for handy log sorting
        in logs folder. Year is on the first place.
        """
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def getCurrDateAndTime() -> str:
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    @staticmethod
    def getCurrDayOfWeek() -> int:
        """Get number of current day of week."""
        return datetime.today().weekday()

    @staticmethod
    def getCurrTimestamp() -> float:
        return datetime.now().timestamp()

    @staticmethod
    def getPastTimestamp(days_count) -> float:
        """Get timestamp of past moment by days count.

        @param days_count Backwards days count.
        """
        return (datetime.now() - timedelta(days=days_count)).timestamp()

    @staticmethod
    def sleep(delta):
        sleep(delta)
