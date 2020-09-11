from Migrations.Migration import Migration
from Controllers.Log.LogController import LogController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class TelegramUsersTableMigration(Migration):

    logger = LogController()

    def getDescription(self):
        print("Create UsersTable migration")

    # If you will change amount of fields here
    # do not forget to update new indices at Controllers/UserController
    def up(self):
        query = '''CREATE TABLE telegramUsers (
                user_id INTEGER PRIMARY KEY,
                chat_id INTEGER NOT NULL,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                language_code TEXT,
                is_bot BOOLEAN,
                is_alive BOOLEAN,
                registration_date DATETIME default current_timestamp,
                university_id INTEGER,
                group_id INTEGER);'''

        SqlLiteDbController().submitQuery(query)
        self.logger.info("TelegramUsersTableMigration up")

    def down(self):
        query = '''DROP TABLE telegramUsers;'''
        SqlLiteDbController().submitQuery(query)
        self.logger.info("TelegramUsersTableMigration down")
