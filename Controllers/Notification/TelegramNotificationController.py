import os

from Controllers.DateTimeController import DateTimeController
from Controllers.Notification.NotificationController import NotificationController


class TelegramNotificationController(NotificationController):

    max_connection_time = 1

    log_name_pattern = 'telegram_notification_%s.log'

    tg_api_url = 'https://api.telegram.org/bot%s/sendMessage'

    def __init__(self, config):
        self.config = config

    def sendMessage(self, message):
        command = self.buildCommand(message)
        filepath = self.getLogFilename()
        os.system(command + " >> " + filepath)
        os.system("echo" + " >> " + filepath)  # used to prevent json reply in cmd

    def getLogFilename(self):
        """Get logfile name for telegram reply log.

        Telegram replies on each message that was sent by curl with
        parameters array. So we store this replies as additional logs.

        @return Built log name.
        """
        return self.config.LOGS_FOLDER + self.log_name_pattern % DateTimeController.getCurrDate()

    def buildUrl(self):
        """Build telegram api url to send notification message."""
        return self.tg_api_url % self.config.MONITORING_BOT_TOKEN

    def buildCommand(self, message):
        """Build curl cli command to send message to telegram notification bot."""
        return f'curl -s -X POST {self.buildUrl()} ' \
               f'--max-time {self.max_connection_time} ' \
               f'-d chat_id={self.config.NOTIFICATION_CHAT_ID}  ' \
               f'-d text=\"{message}\"'
