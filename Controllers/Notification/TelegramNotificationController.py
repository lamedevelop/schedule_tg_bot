import os

from Controllers.DateTimeController import DateTimeController
from Controllers.Notification.NotificationController import NotificationController


class TelegramNotificationController(NotificationController):

    max_connection_time = 1

    log_filename = 'Logs/telegram_notification_%s.log'

    def __init__(self, config):
        self.token = config.MONITORING_BOT_TOKEN,
        self.chat_id = config.NOTIFICATION_CHAT_ID

    def sendMessage(self, message):
        command = self.buildCommand(message)
        filepath = self.log_filename % DateTimeController.getCurrDate()
        os.system(command + " >> " + filepath)
        os.system("echo" + " >> " + filepath)  # used to prevent json reply in cmd

    def buildUrl(self):
        return f'https://api.telegram.org/bot{self.token}/sendMessage'

    def buildCommand(self, message):
        url = self.buildUrl()
        return f'curl -s -X POST {url} ' \
               f'--max-time {self.max_connection_time} ' \
               f'-d chat_id={self.chat_id}  ' \
               f'-d text=\"{message}\"'
