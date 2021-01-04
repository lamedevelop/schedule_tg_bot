from Database.Migrations.Migration import Migration
from Database.Models.UniversityModel import UniversityModel

from Controllers.Log.LogController import LogController
from Controllers.SqlLiteDbController import SqlLiteDbController


class UniversitiesTableMigration(Migration):

    logger = LogController()

    def getDescription(self):
        print("Create UniversitiesTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + UniversityModel.table_name + ''' (
                university_id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL);'''

        SqlLiteDbController().submitQuery(query)
        self.logger.info("UniversitiesTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + UniversityModel.table_name + ';'
        SqlLiteDbController().submitQuery(query)
        self.logger.info("UniversitiesTableMigration down")
