from Controllers.Notification.TelegramNotificationController import TelegramNotificationController


class NotificationManager:
    notifiers = {
        "teleram": TelegramNotificationController()
    }