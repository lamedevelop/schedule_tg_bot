from Database.Models.GroupModel import GroupModel
from Database.Migrations.Migration import Migration
from Controllers.Log.LogController import LogController
from Controllers.SqlLiteDbController import SqlLiteDbController


class GroupsTableMigration(Migration):

    def getDescription(self):
        print("Create GroupsTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + GroupModel.table_name + ''' (
                group_id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_name TEXT NOT NULL,
                university_id INTEGER,
                schedule_text TEXT,
                schedule_url TEXT,
                update_date INTEGER);'''

        SqlLiteDbController().submitQuery(query)
        LogController().info("GroupsTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + GroupModel.table_name + ';'
        SqlLiteDbController().submitQuery(query)
        LogController().info("GroupsTableMigration down")
