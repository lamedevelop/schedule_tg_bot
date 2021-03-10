from Database.Migrations.Migration import Migration
from Database.Models.UserMessageModel import UserMessageModel


class UserMessagesTableMigration(Migration):

    def getDescription(self):
        print("Create RandomMessagesTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + UserMessageModel.table_name + ''' (
                message_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                chat_id INTEGER,
                user_status INTEGER,
                message BLOB,
                creation_date INTEGER);'''

        self.dbController.submitQuery(query)
        self.logger.info("UserMessagesTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + UserMessageModel.table_name + ';'
        self.dbController.submitQuery(query)
        self.logger.info("UserMessagesTableMigration down")
