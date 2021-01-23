import ssl
import smtplib

from Controllers.Notification.NotificationController import NotificationController


class MailNotificationController(NotificationController):

    def __init__(self, config):
        self.sender_email = config.MAIL_SENDER
        self.receiver_email = config.MAIL_RECEIVERS
        self.password = config.MAIL_PASSWORD
        self.port = config.MAIL_PORT
        self.smtp_server = config.MAIL_SMTP_SERVER

    def sendMessage(self, message):
        message = f"""Subject: Schedule error occurred
This message was automatically sent from schedule_tg_bot server.
Error message:
{message}
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
