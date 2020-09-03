from SqlLiteDbController import SqlLiteDbController
from Migrations.Migration import Migration


class UniversitiesTableMigration(Migration):

    def getDescription(self):
        print("Create UniversitiesTable migration")


    def up(self):
        query = '''CREATE TABLE universities (
                university_id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL);'''

        SqlLiteDbController().submitQuery(query)
        print("UniversitiesTableMigration up")


    def down(self):
        query = '''DROP TABLE universities;'''
        SqlLiteDbController().submitQuery(query)
        print("UniversitiesTableMigration down")
