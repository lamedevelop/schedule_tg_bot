from abc import ABCMeta, abstractmethod, abstractproperty


class NotificationController:
    __metaclass__ = ABCMeta

    @abstractmethod
    def sendMessage(self, message):
        pass
