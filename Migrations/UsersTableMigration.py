from Migrations.Migration import Migration


class UsersTableMigration(Migration):

    def __init__(self):
        pass


    def getDescription(self):
        print("Create UsersTable migration")


    def up(self):
    	print("UsersTable up")


    def down(self):
    	print("UsersTable down")
