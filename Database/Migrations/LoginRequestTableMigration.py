from Database.Models.GroupModel import GroupModel
from Database.Migrations.Migration import Migration
from Database.Models.LoginRequestModel import LoginRequestModel


class LoginRequestTableMigration(Migration):

    def getDescription(self):
        print("Create LoginRequest migration")

    def up(self):
        query = '''CREATE TABLE ''' + LoginRequestModel.table_name + ''' (
                request_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                group_id INTEGER NOT NULL,
                university_id INTEGER NOT NULL,
                client_ip TEXT,
                update_date INTEGER);'''

        self.dbController.submitQuery(query)
        self.logger.info("LoginRequestTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + LoginRequestModel.table_name + ';'
        self.dbController.submitQuery(query)
        self.logger.info("LoginRequestTableMigration down")
