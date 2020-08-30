from Migrations.Migration import Migration


class RandomMessagesTableMigration(Migration):

    def __init__(self):
        pass


    def getDescription(self):
        print("Create RandomMessagesTable migration")


    def up(self):
        print("RandomMessagesTableMigration up")


    def down(self):
        print("RandomMessagesTableMigration down")
