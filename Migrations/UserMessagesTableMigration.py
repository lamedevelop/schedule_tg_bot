from Migrations.Migration import Migration
from Controllers.Log.LogController import LogController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class UserMessagesTableMigration(Migration):

    logger = LogController()

    def getDescription(self):
        print("Create RandomMessagesTable migration")

    def up(self):
        query = '''CREATE TABLE userMessages (
                message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                user_status INTEGER,
                message TEXT,
                creation_date DATETIME default current_timestamp);'''

        SqlLiteDbController().submitQuery(query)
        self.logger.info("UserMessagesTableMigration up")

    def down(self):
        query = '''DROP TABLE userMessages;'''
        SqlLiteDbController().submitQuery(query)
        self.logger.info("UserMessagesTableMigration down")
