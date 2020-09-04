from Migrations.Migration import Migration
from Controllers.Log.LogController import LogController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class TelegramUsersTableMigration(Migration):

    logger = LogController()

    def getDescription(self):
        print("Create UsersTable migration")

    def up(self):
        query = '''CREATE TABLE telegramUsers (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                language_code TEXT,
                is_bot BOOLEAN,
                registration_date DATETIME default current_timestamp,
                university_id INTEGER,
                group_id INTEGER);'''

        SqlLiteDbController().submitQuery(query)
        self.logger.info("TelegramUsersTableMigration up")

    def down(self):
        query = '''DROP TABLE telegramUsers;'''
        SqlLiteDbController().submitQuery(query)
        self.logger.info("TelegramUsersTableMigration down")
