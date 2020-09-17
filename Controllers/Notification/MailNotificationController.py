import smtplib, ssl
from Controllers.Notification.NotificationController import NotificationController


class MailNotificationController(NotificationController):

    def __init__(self):
        self.port = 465
        self.smtp_server = "smtp.mail.ru"
        self.sender_email = "schedulebot@mail.ru"
        self.receiver_email = "receiver@mail.ru"
        self.password = "default_password"

    def sendMessage(self, message):
        message = """\
Subject: Hi there
This message is sent from Python.
"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
                self.smtp_server,
                self.port,
                context=context
        ) as server:

            server.login(
                self.sender_email,
                self.password
            )

            server.sendmail(
                self.sender_email,
                self.receiver_email,
                message
            )
