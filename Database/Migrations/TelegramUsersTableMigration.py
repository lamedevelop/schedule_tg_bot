from Database.Migrations.Migration import Migration
from Database.Models.TelegramUserModel import TelegramUserModel

from Controllers.Log.LogController import LogController
from Controllers.SqlLiteDbController import SqlLiteDbController


class TelegramUsersTableMigration(Migration):

    logger = LogController()

    def getDescription(self):
        print("Create UsersTable migration")

    # If you will change amount of fields here
    # do not forget to update new indices at Controllers/UserController
    def up(self):
        query = '''CREATE TABLE ''' + TelegramUserModel.table_name + ''' (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                language_code TEXT,
                is_bot BOOLEAN,
                is_alive BOOLEAN,
                registration_date DATETIME default current_timestamp,
                university_id INTEGER,
                group_id INTEGER,
                CONSTRAINT AK_chat_id UNIQUE(chat_id));'''

        SqlLiteDbController().submitQuery(query)
        self.logger.info("TelegramUsersTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + TelegramUserModel.table_name + ';'
        SqlLiteDbController().submitQuery(query)
        self.logger.info("TelegramUsersTableMigration down")
