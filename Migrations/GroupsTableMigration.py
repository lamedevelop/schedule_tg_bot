from SqlLiteDbController import SqlLiteDbController
from Migrations.Migration import Migration


class GroupsTableMigration(Migration):

    def __init__(self):
        self.dbControler = SqlLiteDbController()


    def getDescription(self):
        print("Create GroupsTable migration")


    def up(self):
        query = '''CREATE TABLE groups (
                group_id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_name TEXT NOT NULL,
                university_id INTEGER,
                schedule_text TEXT,
                schedule_url TEXT,
                update_date DATETIME default current_timestamp);'''
        self.dbControler.submitQuery(query)
        print("GroupsTableMigration up")


    def down(self):
        query = '''DROP TABLE groups;'''
        self.dbControler.submitQuery(query)
        print("GroupsTableMigration down")
