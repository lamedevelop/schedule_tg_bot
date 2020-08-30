from Migrations.Migration import Migration


class UniversitiesTableMigration(Migration):

    def __init__(self):
        pass


    def getDescription(self):
        print("Create UniversitiesTable migration")


    def up(self):
        print("UniversitiesTableMigration up")


    def down(self):
        print("UniversitiesTableMigration down")
