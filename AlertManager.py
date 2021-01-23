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

    def __init__(self):
        config = CliArgsController.getConfig()
        self.notifiers = [
            MailNotificationController(config),
            TelegramNotificationController(config),
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

    @staticmethod
    def mail_test():
        mailer = MailNotificationController()
        mailer.sendMessage("Hello!!!!")
