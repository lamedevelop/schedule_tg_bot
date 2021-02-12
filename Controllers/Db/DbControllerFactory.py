from Controllers.Db.MariadbDbController import MariadbDbController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class DbControllerFactory:

    @staticmethod
    def getDbController():
        """Controller generator

        @return instance of AbstractDbController
        """
        return MariadbDbController()
