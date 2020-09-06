from Configs.tgConfig import MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID
from Controllers.Notification.MailNotificationController import MailNotificationController
from Controllers.Notification.TelegramNotificationController import TelegramNotificationController


class NotificationManager:
    problem_levels = {
        0: "Info",
        1: "Normal",
        2: "Disaster"
    }

    def __init__(self):
        self.notifiers = [
            TelegramNotificationController(MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID),
        ]

    def notify(self, message, severity=None):
        # if severity and severity in self.problem_levels.keys():
        #     message += f'\n\n Severity: {self.problem_levels.get(severity)}'

        for notifier in self.notifiers:
            notifier.notify(message)
