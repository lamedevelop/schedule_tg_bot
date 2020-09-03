from abc import ABC, abstractmethod, abstractproperty


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
