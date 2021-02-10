from Database.Models.GroupModel import GroupModel
from Database.Migrations.Migration import Migration


class GroupsTableMigration(Migration):

    def getDescription(self):
        print("Create GroupsTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + GroupModel.table_name + ''' (
                group_id INTEGER NOT NULL AUTO_INCREMENT,
                group_name TEXT NOT NULL,
                university_id INTEGER,
                schedule_text TEXT,
                schedule_url TEXT,
                update_date INTEGER,
                PRIMARY KEY (group_id));'''

        self.dbController.submitQuery(query)
        self.logger.info("GroupsTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + GroupModel.table_name + ';'
        self.dbController.submitQuery(query)
        self.logger.info("GroupsTableMigration down")
