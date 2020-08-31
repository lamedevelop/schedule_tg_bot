from Migrations.GroupsTableMigration import GroupsTableMigration
from Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration
from Migrations.RandomMessagesTableMigration import RandomMessagesTableMigration

from DbController import DbController


class DbManager:

    migrations = [
        GroupsTableMigration(),
        UniversitiesTableMigration(),
        TelegramUsersTableMigration(),
        RandomMessagesTableMigration()
    ]

    
    def __init__(self):
        pass


    def addUniversity(self, university_name="МГТУ"):
        query = "INSERT INTO universities (university_name) VALUES ({})".format(university_name)
        DbController().submitQuery(query)


    def getUniversities(self):
        query = "SELECT university_name FROM universities"
        return DbController().fetchQuery(query)


    def upAllMigrations(self):
        for migration in self.migrations:
            migration.up()


    def downAllMigrations(self):
        for migration in self.migrations:
            migration.down()


    def getDescriptionForAllMigrations(self):
        for migration in self.migrations:
            migration.getDescription()
