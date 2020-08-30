from DbController import DbController
from Migrations.Migration import Migration


class UniversitiesTableMigration(Migration):

    def __init__(self):
        self.dbControler = DbController()


    def getDescription(self):
        print("Create UniversitiesTable migration")


    def up(self):
        query = '''CREATE TABLE universities (
                university_id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL);'''
        self.dbControler.runQuery(query)
        print("UniversitiesTableMigration up")


    def down(self):
        query = '''DROP TABLE universities;'''
        self.dbControler.runQuery(query)
        print("UniversitiesTableMigration down")
