from DbController import DbController
from Migrations.Migration import Migration


class UsersTableMigration(Migration):

    def __init__(self):
        self.dbControler = DbController()


    def getDescription(self):
        print("Create UsersTable migration")


    def up(self):
        query = '''CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                language_code TEXT,
                is_bot BOOLEAN,
                registration_date DATETIME default current_timestamp,
                university_id INTEGER,
                group_id INTEGER);'''

        self.dbControler.runQuery(query)
        print("UsersTable up")


    def down(self):
        query = '''DROP TABLE users;'''
        self.dbControler.runQuery(query)
        print("UsersTable down")
