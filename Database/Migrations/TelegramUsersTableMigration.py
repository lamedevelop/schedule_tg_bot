from Database.Migrations.Migration import Migration
from Database.Models.TelegramUserModel import TelegramUserModel

from Controllers.Log.LogController import LogController
from Controllers.SqlLiteDbController import SqlLiteDbController


class TelegramUsersTableMigration(Migration):

    def getDescription(self):
        print("Create UsersTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + TelegramUserModel.table_name + ''' (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                language_code TEXT DEFAULT 'en',
                is_bot BOOLEAN,
                is_alive BOOLEAN,
                registration_date INTEGER,
                university_id INTEGER,
                group_id INTEGER,
                CONSTRAINT AK_chat_id UNIQUE(chat_id));'''

        SqlLiteDbController().submitQuery(query)
        LogController().info("TelegramUsersTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + TelegramUserModel.table_name + ';'
        SqlLiteDbController().submitQuery(query)
        LogController().info("TelegramUsersTableMigration down")
