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

    def addUniversity(self, university_name):
        query = DbQueriesController().getInsertQuery("universities", "university_name", university_name)
        SqlLiteDbController().submitQuery(query)

    def getUniversities(self):
        query = DbQueriesController().getSelectQuery("university_name", "universities")
        return SqlLiteDbController().fetchQuery(query)

    def getUniversityIdByName(self, name):
        query = DbQueriesController().getSelectWithParamQuery("university_id", "universities", "university_name", name)
        return SqlLiteDbController().fetchQuery(query)

    def addGroup(self, groupInfo):
        query = DbQueriesController().getGroupInsertQuery(groupInfo)
        SqlLiteDbController().submitQuery(query)

    def getGroupsByUniversityId(self, universityId):
        query = DbQueriesController().getSelectWithParamQuery("group_id, group_name", "groups", "university_id", universityId)
        return SqlLiteDbController().fetchQuery(query)

    def addTgUser(self, userInfo):
        query = DbQueriesController().checkIfExist("telegramUsers", "user_id", userInfo.get("user_id"))
        isExist = SqlLiteDbController().fetchQuery(query)[0][0]

        if (isExist):
            print("user {} exist!".format(userInfo.get("username")))
        else:
            query = DbQueriesController().getUserInsertQuery("telegramUsers", userInfo)
            SqlLiteDbController().submitQuery(query)

    def updateTgUser(self, user_id, paramName, paramVal):
        query = DbQueriesController().getUpdateQuery("telegramUsers", paramName, paramVal, "user_id", user_id)
        SqlLiteDbController().submitQuery(query)

    def getTgUserInfo(self, user_id):
        query = DbQueriesController().getSelectWithParamQuery("*", "telegramUsers", "user_id", user_id)
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
