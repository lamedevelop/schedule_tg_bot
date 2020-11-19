from Database.Migrations.GroupsTableMigration import GroupsTableMigration
from Database.Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Database.Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration
from Database.Migrations.UserMessagesTableMigration import UserMessagesTableMigration

from Database.Models.GroupModel import GroupModel
from Database.Models.TelegramUserModel import TelegramUserModel
from Database.Models.UniversityModel import UniversityModel
from Database.Models.UserMessageModel import UserMessageModel

from Database.ListModels.GroupListModel import GroupListModel
from Database.ListModels.UniversityListModel import UniversityListModel

# from Controllers.Db.DbQueriesController import DbQueriesController
# from Controllers.Db.SqlLiteDbController import SqlLiteDbController

from Controllers.Log.LogController import LogController


class DbManager:

    DEFAULT_GROUP_ID = 0

    migrations = {
        "groupsTableMigration": GroupsTableMigration(),
        "universitiesTableMigration": UniversitiesTableMigration(),
        "telegramUsersTableMigration": TelegramUsersTableMigration(),
        "userMessagesTableMigration": UserMessagesTableMigration()
    }

    # queriesController = DbQueriesController()
    # dbController = SqlLiteDbController()

    logger = LogController()

    @staticmethod
    def run():
        print(UniversityListModel().getListByParams({'university_id': 1}))
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
        UniversityModel({'university_name': university_name}).set()

    @staticmethod
    def getUniversities():
        records = UniversityListModel().getList()
        return [
            {
                'university_id': record.fields['university_id'],
                'university_name': record.fields['university_name'],
            } for record in records
        ]
        # universities = []
        # for record in records:
        #     universities.append(record.fields['university_name'])

    def getUniversityIdByName(self, name: str):
        university = UniversityListModel().getListByParams({'university_name': name})
        return university.fields['university_id']
        # query = self.queriesController.getSelectWithParamQuery("university_id", "universities", "university_name", name)
        # return self.dbController.fetchQuery(query)

    def addGroup(self, groupInfo: dict):
        return GroupModel(groupInfo).set()

    # def getGroupId(self, groupInfo: dict):
    #     query = self.queriesController.getGroupIdQuery(groupInfo.get('group_name'), groupInfo.get('university_id'))
    #
    #     if self.dbController.fetchQuery(query):
    #         return self.dbController.fetchQuery(query)[0][0]
    #
    #     return self.DEFAULT_GROUP_ID

    def getScheduleByGroupId(self, groupId):
        group = GroupModel().get({'group_id': groupId})
        return group.fields['schedule_text']
        # query = DbQueriesController().getSelectWithParamQuery('schedule_text', 'groups', 'group_id', groupId)
        # return SqlLiteDbController().fetchQuery(query)

    def getGroupsByUniversityId(self, universityId):
        records = GroupListModel().getListByParams({'university_id': universityId})
        return [
            {
                'group_id': record.fields['group_id'],
                'group_name': record.fields['group_name'],
            } for record in records
        ]
        # query = self.queriesController.getSelectWithParamQuery("group_id, group_name", "groups", "university_id", universityId)
        # return self.dbController.fetchQuery(query)

    def checkUserExist(self, user_id):
        return bool(TelegramUserModel().get({'user_id': user_id}))

        # query = self.queriesController.checkIfExist("telegramUsers", "user_id", user_id)
        #
        # if self.dbController.fetchQuery(query):
        #     return self.dbController.fetchQuery(query)[0][0]
        #
        # return False

    def addTgUser(self, userInfo: dict):
        TelegramUserModel(userInfo).set()

    def updateTgUser(self, user_id, newFields: dict):
        TelegramUserModel().get(user_id).update(newFields)

    @staticmethod
    def getTgUserInfo(user_id):
        return TelegramUserModel().get(user_id).fields

    def writeUserMessage(self, user_id, user_status, message):
        UserMessageModel({
            'user_id': user_id,
            'user_status': user_status,
            'message': message
        }).set()

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
        UniversityModel({'university_name': 'МЭИ'}).set()
        UniversityModel({'university_name': 'МГТУ'}).set()
        DbManager.logger.info("Db written with test data. Delete before deploy!")

    @staticmethod
    def resetDb():
        DbManager.downAllMigrations()
        DbManager.upAllMigrations()
        DbManager.fillTestData()
