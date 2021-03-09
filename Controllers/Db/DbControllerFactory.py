from Controllers.Db.MariaDbController import MariaDbController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class DbControllerFactory:

    @staticmethod
    def getDbController():
        """Controller generator

        @return instance of AbstractDbController
        """
        return MariaDbController()
