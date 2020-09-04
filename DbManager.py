from Migrations.GroupsTableMigration import GroupsTableMigration
from Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration
from Migrations.RandomMessagesTableMigration import RandomMessagesTableMigration

from DbQueriesController import DbQueriesController
from SqlLiteDbController import SqlLiteDbController


class DbManager:
    migrations = {
        "groupsTable":          GroupsTableMigration(),
        "universitiesTable":    UniversitiesTableMigration(),
        "tgUsersTable":         TelegramUsersTableMigration(),
        "randomMessagesTable":  RandomMessagesTableMigration()
    }

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
        for migration in self.migrations.items():
            migration[1].up()

    def downAllMigrations(self):
        for migration in self.migrations.items():
            migration[1].down()

    def getDescriptionForAllMigrations(self):
        for migration in self.migrations.items():
            migration[1].getDescription()

    # Fill test data to db
    # Use only on empty db for testing
    def fillTestData(self):
        # Fill test 2 universities
        university_name = "MPEI"
        query = DbQueriesController().getInsertQuery("universities", "university_name", university_name)
        SqlLiteDbController().submitQuery(query)

        university_name = "BMSTU"
        query = DbQueriesController().getInsertQuery("universities", "university_name", university_name)
        SqlLiteDbController().submitQuery(query)

        # Fill test 2 groups
        groupInfo = {
            "group_name": "A-06M-20",
            "university_id": 1,
            "schedule_text": "Mpei schedule test",
            "schedule_url": "mpei.ru"
        }
        query = DbQueriesController().getGroupInsertQuery(groupInfo)
        SqlLiteDbController().submitQuery(query)

        groupInfo = {
            "group_name": "IU3-13B",
            "university_id": 2,
            "schedule_text": "Bmstu schedule test",
            "schedule_url": "bmstu.ru"
        }
        query = DbQueriesController().getGroupInsertQuery(groupInfo)
        SqlLiteDbController().submitQuery(query)

        print("Db written with test data. Delete before deploy!")

    def renewDb(self):
        self.downAllMigrations(self)
        self.upAllMigrations(self)
        self.fillTestData(self)
