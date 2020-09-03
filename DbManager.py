from Migrations.GroupsTableMigration import GroupsTableMigration
from Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration
from Migrations.RandomMessagesTableMigration import RandomMessagesTableMigration

from DbQueriesController import DbQueriesController
from SqlLiteDbController import SqlLiteDbController


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
        query = DbQueriesController().getInsertQuery("universities", "university_name", university_name)
        SqlLiteDbController().submitQuery(query)


    def getUniversities(self):
        query = DbQueriesController().getSelectQuery("university_name", "universities")
        return SqlLiteDbController().fetchQuery(query)


    # Migrations methods
    def upAllMigrations(self):
        for migration in self.migrations:
            migration.up()


    def downAllMigrations(self):
        for migration in self.migrations:
            migration.down()


    def getDescriptionForAllMigrations(self):
        for migration in self.migrations:
            migration.getDescription()
