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

    def addUniversity(self, university_name="МГТУ"):
        query = DbQueriesController().getInsertQuery("universities", "university_name", university_name)
        SqlLiteDbController().submitQuery(query)

    def getUniversities(self):
        query = DbQueriesController().getSelectQuery("university_name", "universities")
        return SqlLiteDbController().fetchQuery(query)

    def getUniversityIdByName(self, name):
        query = DbQueriesController().getSelectWithParamQuery("university_id", "universities", "university_name", name)
        return SqlLiteDbController().fetchQuery(query)

    def addUser(self, userInfo):
        query = DbQueriesController().checkIfExist("telegramUsers", "user_id", userInfo.get("user_id"))
        isExist = SqlLiteDbController().fetchQuery(query)[0][0]

        if (isExist):
            print("user {} exist!".format(userInfo.get("username")))
        else:
            query = DbQueriesController().getUserInsertQuery("telegramUsers", userInfo)
            SqlLiteDbController().submitQuery(query)

    def updateUser(self, paramName, paramVal):
        query = DbQueriesController().getInsertQuery("telegramUsers", paramName, paramVal)
        SqlLiteDbController().submitQuery(query)

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
