from abc import ABCMeta, abstractmethod, abstractproperty


class NotificationController:
    __metaclass__ = ABCMeta

    @abstractmethod
    def sendMessage(self, message: str):
        """Send notification message to bot developer.

        Used in mail and telegram notifications.

        @param message Notification message.
        """
        pass
