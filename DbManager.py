from Migrations.GroupsTableMigration import GroupsTableMigration
from Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration
from Migrations.UserMessagesTableMigration import UserMessagesTableMigration

from Controllers.Db.DbQueriesController import DbQueriesController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController

from Controllers.Log.LogController import LogController


class DbManager:

    migrations = {
        "groupsTable":          GroupsTableMigration(),
        "universitiesTable":    UniversitiesTableMigration(),
        "tgUsersTable":         TelegramUsersTableMigration(),
        "userMessagesTable":  UserMessagesTableMigration()
    }

    queriesController = DbQueriesController()
    dbController = SqlLiteDbController()

    logger = LogController()

    def addUniversity(self, university_name: str):
        query = self.queriesController.getInsertQuery("universities", "university_name", university_name)
        self.dbController.submitQuery(query)

    def getUniversities(self):
        query = self.queriesController.getSelectQuery("university_name", "universities")
        return self.dbController.fetchQuery(query)

    def getUniversityIdByName(self, name: str):
        query = self.queriesController.getSelectWithParamQuery("university_id", "universities", "university_name", name)
        return self.dbController.fetchQuery(query)

    def addGroup(self, groupInfo: dict):
        query = self.queriesController.getGroupInsertQuery(groupInfo)
        self.dbController.submitQuery(query)

    def getGroupId(self, groupInfo: dict):
        query = self.queriesController.getGroupIdQuery(groupInfo.get('group_name'), groupInfo.get('university_id'))
        return self.dbController.fetchQuery(query)[0][0]

    def getGroupsByUniversityId(self, universityId):
        query = self.queriesController.getSelectWithParamQuery("group_id, group_name", "groups", "university_id", universityId)
        return self.dbController.fetchQuery(query)

    def addTgUser(self, userInfo: dict):
        query = self.queriesController.checkIfExist("telegramUsers", "user_id", userInfo.get("user_id"))
        isExist = self.dbController.fetchQuery(query)[0][0]

        if (isExist):
            self.logger.info("user {} exist!".format(userInfo.get("username")))
        else:
            query = self.queriesController.getUserInsertQuery("telegramUsers", userInfo)
            self.dbController.submitQuery(query)

    def updateTgUser(self, user_id, paramName: str, paramVal):
        query = self.queriesController.getUpdateQuery("telegramUsers", paramName, paramVal, "user_id", user_id)
        self.dbController.submitQuery(query)

    def getTgUserInfo(self, user_id):
        query = self.queriesController.getSelectWithParamQuery("*", "telegramUsers", "user_id", user_id)
        return self.dbController.fetchQuery(query)

    def writeUserMessage(self, user_id, message):
        query = self.queriesController.getMessageInsertQuery(user_id, message)
        self.dbController.submitQuery(query)

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
    # todo: Move to unit test later
    @staticmethod
    def fillTestData(self):
        # Fill test 2 universities
        university_name = "MPEI"
        self.addUniversity(self, university_name)

        university_name = "BMSTU"
        self.addUniversity(self, university_name)

        # Fill test 2 groups
        groupInfo = {
            "group_name": "A-06M-20".lower(),
            "university_id": 1,
            "schedule_text": "Mpei schedule test",
            "schedule_url": "mpei.ru"
        }
        self.addGroup(self, groupInfo)

        groupInfo = {
            "group_name": "IU3-13B".lower(),
            "university_id": 2,
            "schedule_text": "Bmstu schedule test",
            "schedule_url": "bmstu.ru"
        }
        self.addGroup(self, groupInfo)

        self.logger.info("Db written with test data. Delete before deploy!")

    @staticmethod
    def resetDb(self):
        self.downAllMigrations(self)
        self.upAllMigrations(self)
        self.fillTestData(self)

    @staticmethod
    def dropDb(self):
        self.dbController.dropDb()
