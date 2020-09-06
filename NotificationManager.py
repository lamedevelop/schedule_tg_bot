from Configs.tgConfig import MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID
from Controllers.Date.DateTimeController import DateTimeController
from Controllers.Notification.MailNotificationController import MailNotificationController
from Controllers.Notification.TelegramNotificationController import TelegramNotificationController


class NotificationManager:

    INFO_LEVEL = 1
    WARNING_LEVEL = 2
    DISASTER_LEVEL = 3

    problem_levels = {
        INFO_LEVEL: "Info",
        WARNING_LEVEL: "Warning",
        DISASTER_LEVEL: "Disaster"
    }

    def __init__(self):
        self.notifiers = [
            TelegramNotificationController(MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID),
        ]

    def info(self, message, severity=None):
        header = f'[INFO] {DateTimeController.getCurrDateAndTime()}\n' \
                 + self.getSeverity(severity)
        print(self.getSeverity(severity))
        print(header)
        message = header + message
        self.notify(message)

    def alert(self, message, severity=None):
        header = f'[ALERT] {DateTimeController.getCurrDateAndTime()}\n' \
                 + self.getSeverity(severity)
        message = header + message
        self.notify(message)

    def notify(self, message):
        for notifier in self.notifiers:
            notifier.notify(message)

    def getSeverity(self, severity):
        if severity and severity in self.problem_levels.keys():
            return f'Severity: {self.problem_levels.get(severity)}\n'
        else:
            return ""
