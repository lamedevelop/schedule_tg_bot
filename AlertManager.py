from Controllers.CliArgsController import CliArgsController
from Controllers.Log.DumpController import DumpController
from Controllers.DateTimeController import DateTimeController
from Controllers.Notification.MailNotificationController import MailNotificationController
from Controllers.Notification.TelegramNotificationController import TelegramNotificationController


class AlertManager:

    INFO_LEVEL = 1
    WARNING_LEVEL = 2
    DISASTER_LEVEL = 3

    problem_levels = {
        INFO_LEVEL: "INFO",
        WARNING_LEVEL: "WARNING",
        DISASTER_LEVEL: "DISASTER"
    }

    mail_notifier = 0
    telegram_notifier = 1

    def __init__(self):
        config = CliArgsController.getConfig()
        self.notifiers = {
            self.mail_notifier: MailNotificationController(config),
            self.telegram_notifier: TelegramNotificationController(config),
        }

    def notify(self, message, severity=None):
        message = self.getHeader(severity) + message
        self.notifiers[self.telegram_notifier].sendMessage(message)
        if severity >= self.WARNING_LEVEL:
            self.notifiers[self.mail_notifier].sendMessage(message)

    def getHeader(self, severity):
        if severity and severity in self.problem_levels.keys():
            return f'[{self.problem_levels.get(severity)}] {DateTimeController.getCurrDateAndTime()}\n'
        else:
            return ""

    @staticmethod
    def dump():
        DumpController().dump()
