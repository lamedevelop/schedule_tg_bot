from Database.Migrations.Migration import Migration
from Controllers.Log.LogController import LogController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class GroupsTableMigration(Migration):

    logger = LogController()

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

        SqlLiteDbController().submitQuery(query)
        self.logger.info("GroupsTableMigration up")

    def down(self):
        query = '''DROP TABLE groups;'''
        SqlLiteDbController().submitQuery(query)
        self.logger.info("GroupsTableMigration down")
