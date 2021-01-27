from abc import ABC, abstractmethod

from Controllers.Log.LogController import LogController
from Controllers.Db.DbFactoryController import DbFactoryController


class Migration(ABC):

    def __init__(self):
        self.dbController = DbFactoryController.getDbController()
        self.logger = LogController()

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass
