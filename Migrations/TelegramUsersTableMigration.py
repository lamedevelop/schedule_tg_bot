from Controllers.Db.SqlLiteDbController import SqlLiteDbController
from Migrations.Migration import Migration


class TelegramUsersTableMigration(Migration):

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
        print("TelegramUsersTableMigration up")

    def down(self):
        query = '''DROP TABLE telegramUsers;'''
        SqlLiteDbController().submitQuery(query)
        print("TelegramUsersTableMigration down")
