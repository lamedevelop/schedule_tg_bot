from Migrations.Migration import Migration


class GroupsTableMigration(Migration):

    def __init__(self):
        pass


    def getDescription(self):
        print("Create GroupsTable migration")


    def up(self):
        print("GroupsTableMigration up")


    def down(self):
        print("GroupsTableMigration down")
