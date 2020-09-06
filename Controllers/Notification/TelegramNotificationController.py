import os

from Controllers.Notification.NotificationController import NotificationController


class TelegramNotificationController(NotificationController):

    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def sendMessage(self, message):
        command = self.buildCommand(message)
        os.system(command)

    def buildUrl(self):
        return f'https://api.telegram.org/bot{self.token}/sendMessage'

    def buildCommand(self, message):
        url = self.buildUrl()
        return f'curl -s -X POST {url}  -d chat_id={self.chat_id}  -d text=\"{message}\"'
