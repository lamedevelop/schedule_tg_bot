from DbController import DbController
from Migrations.Migration import Migration


class RandomMessagesTableMigration(Migration):

    def __init__(self):
        self.dbControler = DbController()


    def getDescription(self):
        print("Create RandomMessagesTable migration")


    def up(self):
        query = '''CREATE TABLE randomMessages (
                message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                message TEXT,
                creation_date DATETIME default current_timestamp);'''
        self.dbControler.runQuery(query)
        print("RandomMessagesTableMigration up")


    def down(self):
        query = '''DROP TABLE randomMessages;'''
        self.dbControler.runQuery(query)
        print("RandomMessagesTableMigration down")
