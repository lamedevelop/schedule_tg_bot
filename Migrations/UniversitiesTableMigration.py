from SqlLiteDbController import SqlLiteDbController
from Migrations.Migration import Migration


class UniversitiesTableMigration(Migration):

    def __init__(self):
        self.dbControler = SqlLiteDbController()


    def getDescription(self):
        print("Create UniversitiesTable migration")


    def up(self):
        query = '''CREATE TABLE universities (
                university_id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL);'''
        self.dbControler.submitQuery(query)
        print("UniversitiesTableMigration up")


    def down(self):
        query = '''DROP TABLE universities;'''
        self.dbControler.submitQuery(query)
        print("UniversitiesTableMigration down")
