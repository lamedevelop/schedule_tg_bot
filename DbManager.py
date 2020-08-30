from Migrations.UsersTable import UsersTable


class DbManager:

    def __init__(self):
        pass

    def testMigrations(self):
    	a = UsersTable()
    	a.up()


if __name__ == '__main__':
	db = DbManager()
	db.testMigrations()