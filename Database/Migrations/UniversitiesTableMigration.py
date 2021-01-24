from Database.Migrations.Migration import Migration
from Database.Models.UniversityModel import UniversityModel

from Controllers.Log.LogController import LogController
from Controllers.Db.PostgreDbController import PostgreDbController


class UniversitiesTableMigration(Migration):

    def getDescription(self):
        print("Create UniversitiesTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + UniversityModel.table_name + ''' (
                university_id SERIAL PRIMARY KEY,
                university_name TEXT NOT NULL);'''

        PostgreDbController().submitQuery(query)
        LogController().info("UniversitiesTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + UniversityModel.table_name + ';'
        PostgreDbController().submitQuery(query)
        LogController().info("UniversitiesTableMigration down")
