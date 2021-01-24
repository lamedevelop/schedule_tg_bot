from Database.Models.GroupModel import GroupModel
from Database.Migrations.Migration import Migration
from Controllers.Log.LogController import LogController
from Controllers.Db.PostgreDbController import PostgreDbController


class GroupsTableMigration(Migration):

    def getDescription(self):
        print("Create GroupsTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + GroupModel.table_name + ''' (
                group_id SERIAL PRIMARY KEY ,
                group_name TEXT NOT NULL,
                university_id INTEGER,
                schedule_text TEXT,
                schedule_url TEXT,
                update_date INTEGER);'''

        PostgreDbController().submitQuery(query)
        LogController().info("GroupsTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + GroupModel.table_name + ';'
        PostgreDbController().submitQuery(query)
        LogController().info("GroupsTableMigration down")
