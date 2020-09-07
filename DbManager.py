from Migrations.GroupsTableMigration import GroupsTableMigration
from Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration
from Migrations.UserMessagesTableMigration import UserMessagesTableMigration

from Controllers.Db.DbQueriesController import DbQueriesController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController

from Controllers.Log.LogController import LogController


class DbManager:

    migrations = {
        "groupsTableMigration": GroupsTableMigration(),
        "universitiesTableMigration": UniversitiesTableMigration(),
        "telegramUsersTableMigration": TelegramUsersTableMigration(),
        "userMessagesTableMigration": UserMessagesTableMigration()
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

    def getGroupJsonById(self, groupId: dict):
        query = DbQueriesController().getSelectWithParamQuery('schedule_text', 'groups', 'group_id', groupId)
        return SqlLiteDbController().fetchQuery(query)

    def getGroupsByUniversityId(self, universityId):
        query = self.queriesController.getSelectWithParamQuery("group_id, group_name", "groups", "university_id", universityId)
        return self.dbController.fetchQuery(query)

    def addTgUser(self, userInfo: dict):
        query = self.queriesController.checkIfExist("telegramUsers", "user_id", userInfo.get("user_id"))
        isExist = self.dbController.fetchQuery(query)[0][0]

        if isExist:
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
    @staticmethod
    def upMigration(migration):
        DbManager.migrations.get(migration).up()

    @staticmethod
    def downMigration(migration):
        DbManager.migrations.get(migration).down()

    @staticmethod
    def upAllMigrations():
        for migration in DbManager.migrations.items():
            migration[1].up()

    @staticmethod
    def downAllMigrations():
        for migration in DbManager.migrations.items():
            migration[1].down()

    @staticmethod
    def getDescriptionForAllMigrations():
        for migration in DbManager.migrations.items():
            migration[1].getDescription()

    # Fill test data to db
    # Use only on empty db for testing
    # todo: Move to unit test later
    @staticmethod
    def fillTestData():
        # Fill test 2 universities
        university_name = "МЭИ"
        DbManager.addUniversity(DbManager(), university_name)
        university_name = "МГТУ"
        DbManager.addUniversity(DbManager(), university_name)
        DbManager.logger.info("Db written with test data. Delete before deploy!")

    @staticmethod
    def resetDb():
        DbManager.downAllMigrations()
        DbManager.upAllMigrations()
        DbManager.fillTestData()

    @staticmethod
    def dropDb():
        DbManager.dbController.dropDb()
