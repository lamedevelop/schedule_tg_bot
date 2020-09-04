from Migrations.Migration import Migration
from Controllers.Log.LogController import LogController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class UniversitiesTableMigration(Migration):

    logger = LogController()

    def getDescription(self):
        print("Create UniversitiesTable migration")

    def up(self):
        query = '''CREATE TABLE universities (
                university_id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL);'''

        SqlLiteDbController().submitQuery(query)
        self.logger.info("UniversitiesTableMigration up")

    def down(self):
        query = '''DROP TABLE universities;'''
        SqlLiteDbController().submitQuery(query)
        self.logger.info("UniversitiesTableMigration down")
