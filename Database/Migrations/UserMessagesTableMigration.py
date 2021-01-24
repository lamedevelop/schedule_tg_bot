from Database.Migrations.Migration import Migration
from Database.Models.UserMessageModel import UserMessageModel

from Controllers.Log.LogController import LogController
from Controllers.Db.PostgreDbController import PostgreDbController


class UserMessagesTableMigration(Migration):

    def getDescription(self):
        print("Create RandomMessagesTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + UserMessageModel.table_name + ''' (
                message_id SERIAL PRIMARY KEY,
                chat_id INTEGER,
                user_status INTEGER,
                message TEXT,
                creation_date INTEGER);'''

        PostgreDbController().submitQuery(query)
        LogController().info("UserMessagesTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + UserMessageModel.table_name + ';'
        PostgreDbController().submitQuery(query)
        LogController().info("UserMessagesTableMigration down")
