from Database.Migrations.Migration import Migration
from Database.Models.UniversityModel import UniversityModel


class UniversitiesTableMigration(Migration):

    def getDescription(self):
        print("Create UniversitiesTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + UniversityModel.table_name + ''' (
                university_id SERIAL PRIMARY KEY,
                university_name TEXT NOT NULL);'''

        self.dbController.submitQuery(query)
        self.logger.info("UniversitiesTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + UniversityModel.table_name + ';'
        self.dbController.submitQuery(query)
        self.logger.info("UniversitiesTableMigration down")
