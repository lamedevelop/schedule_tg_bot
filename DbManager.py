from Migrations.UsersTableMigration import UsersTableMigration
from Migrations.GroupsTableMigration import GroupsTableMigration
from Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Migrations.RandomMessagesTableMigration import RandomMessagesTableMigration

from DbController import DbController


class DbManager:

    migrations = [
        UsersTableMigration(),
        GroupsTableMigration(),
        UniversitiesTableMigration(),
        RandomMessagesTableMigration()
    ]

    
    def __init__(self):
        self.dbController = DbController()


    def upAllMigrations(self):
        for migration in self.migrations:
            migration.up()


    def downAllMigrations(self):
        for migration in self.migrations:
            migration.down()


    def getDescriptionForAllMigrations(self):
        for migration in self.migrations:
            migration.getDescription()


if __name__ == '__main__':
    db = DbManager()
    db.upAllMigrations()
    db.downAllMigrations()
    db.getDescriptionForAllMigrations()
