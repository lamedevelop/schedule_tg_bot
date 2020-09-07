import smtplib, ssl
from Controllers.Notification.NotificationController import NotificationController


class MailNotificationController(NotificationController):

    def sendMessage(self, message):
        port = 465  # For SSL
        smtp_server = "smtp.mail.ru"
        sender_email = "schedulebot@mail.ru"  # Enter your address
        receiver_email = "oleg.gr@outlook.com"  # Enter receiver address
        password = "Ytndpkjvfv43"
        message = """\
        Subject: Hi there

        This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)