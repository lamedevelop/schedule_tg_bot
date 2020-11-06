from Database.Migrations.GroupsTableMigration import GroupsTableMigration
from Database.Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Database.Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration
from Database.Migrations.UserMessagesTableMigration import UserMessagesTableMigration

from Database.Models.GroupModel import GroupModel
from Database.Models.TelegramUserModel import TelegramUserModel
from Database.Models.UniversityModel import UniversityModel
from Database.Models.UserMessageModel import UserMessageModel

from Controllers.Db.DbQueriesController import DbQueriesController
from Controllers.Db.SqlLiteDbController import SqlLiteDbController

from Controllers.Log.LogController import LogController


class DbManager:

    DEFAULT_GROUP_ID = 0

    migrations = {
        "groupsTableMigration": GroupsTableMigration(),
        "universitiesTableMigration": UniversitiesTableMigration(),
        "telegramUsersTableMigration": TelegramUsersTableMigration(),
        "userMessagesTableMigration": UserMessagesTableMigration()
    }

    queriesController = DbQueriesController()
    dbController = SqlLiteDbController()

    logger = LogController()

    @staticmethod
    def run():
        pass
        # message_to_add = [
        #     {
        #         'name': 'user_id',
        #         'value': 11111111
        #     },
        #     {
        #         'name': 'user_status',
        #         'value': 1
        #     },
        #     {
        #         'name': 'message',
        #         'value': 'aaa bbb ccc'
        #     }
        # ]
        #
        # message = UserMessageModel(message_to_add)
        # print(message)
        # print()
        #
        # # message.set()
        #
        # message = UserMessageModel().get(12)
        # print(message)
        # print()
        #
        # user.fields['is_bot'] = 0
        # user.update(user.getSelfFields())
        #
        # user.fields['user_id'] = 123513513513
        # user.fields['chat_id'] = 11
        # print(user.getSelfFields())
        # new_user = TelegramUserModel(user.getSelfFields())
        #
        # print(new_user)
        # new_user.set()
        # new_user.update(
        # [
        #     {
        #         'name': 'is_bot',
        #         'value': 0
        #     }
        # ]
        # )
        #
        # print(new_user)
        # print()

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

        if self.dbController.fetchQuery(query):
            return self.dbController.fetchQuery(query)[0][0]

        return self.DEFAULT_GROUP_ID

    def getGroupJsonById(self, groupId: dict):
        query = DbQueriesController().getSelectWithParamQuery('schedule_text', 'groups', 'group_id', groupId)
        return SqlLiteDbController().fetchQuery(query)

    def getGroupsByUniversityId(self, universityId):
        query = self.queriesController.getSelectWithParamQuery("group_id, group_name", "groups", "university_id", universityId)
        return self.dbController.fetchQuery(query)

    def checkUserExist(self, user_id):
        query = self.queriesController.checkIfExist("telegramUsers", "user_id", user_id)

        if self.dbController.fetchQuery(query):
            return self.dbController.fetchQuery(query)[0][0]

        return False

    def addTgUser(self, userInfo: dict):
        query = self.queriesController.getUserInsertQuery("telegramUsers", userInfo)
        self.dbController.submitQuery(query)

    def updateTgUser(self, user_id, paramName: str, paramVal: str):
        query = self.queriesController.getUpdateQuery("telegramUsers", paramName, paramVal, "user_id", user_id)
        self.dbController.submitQuery(query)

    def getTgUserInfo(self, user_id):
        query = self.queriesController.getSelectWithParamQuery("*", "telegramUsers", "user_id", user_id)
        return self.dbController.fetchQuery(query)

    def writeUserMessage(self, user_id, user_status, message):
        query = self.queriesController.getMessageInsertQuery(user_id, user_status, message)
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
