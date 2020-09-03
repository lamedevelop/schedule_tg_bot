from SqlLiteDbController import SqlLiteDbController
from Migrations.Migration import Migration


class RandomMessagesTableMigration(Migration):

    def getDescription(self):
        print("Create RandomMessagesTable migration")


    def up(self):
        query = '''CREATE TABLE randomMessages (
                message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                message TEXT,
                creation_date DATETIME default current_timestamp);'''

        SqlLiteDbController().submitQuery(query)
        print("RandomMessagesTableMigration up")


    def down(self):
        query = '''DROP TABLE randomMessages;'''
        SqlLiteDbController().submitQuery(query)
        print("RandomMessagesTableMigration down")
