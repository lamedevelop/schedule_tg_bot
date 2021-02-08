from Controllers.Db.PostgreDbController import PostgreDbController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class DbControllerFactory:

    @staticmethod
    def getDbController():
        """Controller generator

        @return instance of AbstractDbController
        """
        return PostgreDbController()
