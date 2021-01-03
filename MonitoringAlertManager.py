from Configs.tgConfig import MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID
from Controllers.Date.DateTimeController import DateTimeController
from Controllers.Log.DumpController import DumpController
from Controllers.Notification.MailNotificationController import MailNotificationController
from Controllers.Notification.TelegramNotificationController import TelegramNotificationController


class MonitoringAlertManager:

    INFO_LEVEL = 1
    WARNING_LEVEL = 2
    DISASTER_LEVEL = 3

    problem_levels = {
        INFO_LEVEL: "INFO",
        WARNING_LEVEL: "WARNING",
        DISASTER_LEVEL: "DISASTER"
    }

    def __init__(self):
        self.notifiers = [
            # MailNotificationController(),
            TelegramNotificationController(MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID),
        ]

    def notify(self, message, severity=None):
        message = self.getHeader(severity) + message
        for notifier in self.notifiers:
            notifier.sendMessage(message)

    def getHeader(self, severity):
        if severity and severity in self.problem_levels.keys():
            return f'[{self.problem_levels.get(severity)}] {DateTimeController.getCurrDateAndTime()}\n'
        else:
            return ""

    @staticmethod
    def dump():
        DumpController().dump()
