from abc import ABC, abstractmethod


class Migration(ABC):

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass
