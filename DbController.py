import os
import sqlite3


class DbController:

    
    dbFilename = 'sqlite.db'


    def __init__(self):
        pass


    def getCursor(self):
        self.sqliteConnection = sqlite3.connect(self.dbFilename)
        self.cursor = sqliteConnection.cursor()


    def execute(self, query):
        self.cursor.execute(query)


    def commit(self):
        self.sqliteConnection.commit()


    def closeConnection(self):
        self.cursor.close()
        self.sqliteConnection.close()


    def db_drop(self, dbFilename=self.dbFilename):
        try:
            os.remove(dbFilename)
            return 'DB was deleted'
        except Exception as e:
            return "Error while deleting db {}".format(e)
