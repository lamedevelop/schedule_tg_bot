import os

from Controllers.DateTimeController import DateTimeController
from Controllers.Notification.NotificationController import NotificationController


class TelegramNotificationController(NotificationController):

    max_connection_time = 1

    log_name_pattern = 'telegram_notification_%s.log'

    def __init__(self, config):
        self.config = config

    def sendMessage(self, message):
        command = self.buildCommand(message)
        filepath = self.getLogFilename()
        os.system(command + " >> " + filepath)
        os.system("echo" + " >> " + filepath)  # used to prevent json reply in cmd

    def getLogFilename(self):
        return self.config.LOGS_FOLDER + self.log_name_pattern % DateTimeController.getCurrDate()

    def buildUrl(self):
        return f'https://api.telegram.org/bot{self.config.MONITORING_BOT_TOKEN}/sendMessage'

    def buildCommand(self, message):
        url = self.buildUrl()
        return f'curl -s -X POST {url} ' \
               f'--max-time {self.max_connection_time} ' \
               f'-d chat_id={self.config.NOTIFICATION_CHAT_ID}  ' \
               f'-d text=\"{message}\"'
