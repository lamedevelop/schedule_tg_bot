from SqlLiteDbController import SqlLiteDbController
from Migrations.Migration import Migration


class UserMessagesTableMigration(Migration):

    def getDescription(self):
        print("Create RandomMessagesTable migration")

    def up(self):
        query = '''CREATE TABLE userMessages (
                message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                message TEXT,
                creation_date DATETIME default current_timestamp);'''

        SqlLiteDbController().submitQuery(query)
        print("UserMessagesTableMigration up")

    def down(self):
        query = '''DROP TABLE userMessages;'''
        SqlLiteDbController().submitQuery(query)
        print("UserMessagesTableMigration down")
