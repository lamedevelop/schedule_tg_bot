import ssl
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from Controllers.Log.LogController import LogController
from Controllers.Notification.NotificationController import NotificationController


class MailNotificationController(NotificationController):

    def __init__(self, config):
        self.sender = config.MAIL_SENDER
        self.receivers = config.MAIL_RECEIVERS
        self.password = config.MAIL_PASSWORD
        self.port = config.MAIL_PORT
        self.smtp_server = config.MAIL_SMTP_SERVER
        self.mail = MIMEMultipart()

    def sendMessage(self, message):
        mail_content = f"""This message was automatically sent from schedule_tg_bot server.

{message}
"""

        self.mail['From'] = self.sender
        self.mail['Subject'] = 'Schedule error occurred'
        self.mail.attach(MIMEText(mail_content, 'plain'))

        self.attachLog()

        for receiver in self.receivers:

            self.mail['To'] = receiver

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(
                    self.smtp_server,
                    self.port,
                    context=context
            ) as server:

                server.login(
                    self.sender,
                    self.password
                )

                server.sendmail(
                    self.sender,
                    receiver,
                    self.mail.as_string()
                )

    def attachLog(self):
        """Attach logfile to email."""

        logfile = LogController().getLogFilename()

        attach_file = open(logfile, 'rb')
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload(attach_file.read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment; filename= www', filename=logfile)

        self.mail.attach(payload)
