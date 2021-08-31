from Controllers.Log.LogController import LogController
from Controllers.DateTimeController import DateTimeController
from Controllers.Db.DbControllerFactory import DbControllerFactory
from Database.Migrations.LoginRequestTableMigration import LoginRequestTableMigration

from Database.Models.GroupModel import GroupModel
from Database.Models.LoginRequestModel import LoginRequestModel
from Database.Models.UniversityModel import UniversityModel
from Database.Models.UserMessageModel import UserMessageModel
from Database.Models.TelegramUserModel import TelegramUserModel

from Database.ListModels.GroupListModel import GroupListModel
from Database.ListModels.UniversityListModel import UniversityListModel
from Database.ListModels.TelegramUserListModel import TelegramUserListModel

from Database.Migrations.GroupsTableMigration import GroupsTableMigration
from Database.Migrations.UniversitiesTableMigration import UniversitiesTableMigration
from Database.Migrations.UserMessagesTableMigration import UserMessagesTableMigration
from Database.Migrations.TelegramUsersTableMigration import TelegramUsersTableMigration


class DbManager:

    @staticmethod
    def addUniversity(university_name: str):
        UniversityModel({'university_name': university_name}).set()

    @staticmethod
    def getUniversities():
        return [university.fields for university in UniversityListModel().getList()]

    @staticmethod
    def getUniversity(university_id):
        return UniversityModel().get(university_id).fields

    @staticmethod
    def getUniversityByName(universityName):
        university = UniversityModel().getUniversityByName(universityName)

        if bool(university):
            return university.fields
        else:
            return []

    @staticmethod
    def addGroup(groupInfo: dict):
        return GroupModel(groupInfo).set()

    @staticmethod
    def getScheduleByGroupId(groupId):
        group = GroupModel().get(groupId)
        return group.fields['schedule_text']

    @staticmethod
    def getGroup(groupInfo):
        group = GroupListModel().getListByParams(groupInfo)

        if bool(group):
            return group[0].fields
        else:
            return []

    @staticmethod
    def updateGroups() -> None:
        from Controllers.Db.ScheduleUpdateController import ScheduleUpdateController
        ScheduleUpdateController.updateGroups()

    @staticmethod
    def updateGroup(group_name) -> None:
        from Controllers.Db.ScheduleUpdateController import ScheduleUpdateController
        ScheduleUpdateController.updateGroupByName(group_name)

    @staticmethod
    def getGroupsByUniversityId(universityId):
        """
        @deprecated Currently deprecated.

        @note Should be fixed before using.

        @param universityId

        @return Bunch of groups by universityId.
        """
        records = GroupListModel().getListByParams({'university_id': universityId})
        return [
            {
                'group_id': record.fields['group_id'],
                'group_name': record.fields['group_name'],
            } for record in records
        ]

    @staticmethod
    def setLoginRequest(requestInfo: dict):
        return LoginRequestModel(requestInfo).set()

    @staticmethod
    def getLoginRequestByClient(client_ip: str):
        return LoginRequestModel().getRequestByClient(client_ip).fields

    @staticmethod
    def dropLoginRequest(request_id: dict):
        return LoginRequestModel().get(request_id).drop()

    @staticmethod
    def checkUserExist(chat_id):
        return bool(TelegramUserListModel().getListByParams({'chat_id': chat_id}))

    @staticmethod
    def addTgUser(userInfo: dict):
        TelegramUserModel(userInfo).set()

    @staticmethod
    def updateTgUser(chat_id, newFields: dict):
        TelegramUserModel().getByChatId(chat_id).update(newFields)

    @staticmethod
    def getTgUserInfo(chat_id):
        return TelegramUserModel().getByChatId(chat_id).fields

    @staticmethod
    def writeUserMessage(messageInfo):
        UserMessageModel(messageInfo).set()

    @staticmethod
    def connectDb():
        DbControllerFactory.getDbController().connectToDb()

    @staticmethod
    def checkDbAvailability():
        return DbControllerFactory.getDbController().checkConnection()

    @staticmethod
    def startupDb():
        while not DbManager.checkDbAvailability():
            LogController().alert('Db unavailable. Waiting 5 seconds for connection')
            DateTimeController.sleep(5)
        DbManager.upAllMigrations()
        DbManager.fillGroups()

    @staticmethod
    def getMigrations():
        return {
            "groupsTableMigration": GroupsTableMigration(),
            "universitiesTableMigration": UniversitiesTableMigration(),
            "telegramUsersTableMigration": TelegramUsersTableMigration(),
            "userMessagesTableMigration": UserMessagesTableMigration(),
            "loginRequestTableMigration": LoginRequestTableMigration(),
        }

    # Migrations methods
    @staticmethod
    def upMigration(migration):
        DbManager.getMigrations().get(migration).up()

    @staticmethod
    def downMigration(migration):
        DbManager.getMigrations().get(migration).down()

    @staticmethod
    def upAllMigrations():
        for migration in DbManager.getMigrations():
            DbManager.getMigrations()[migration].up()

    @staticmethod
    def downAllMigrations():
        for migration in DbManager.getMigrations():
            DbManager.getMigrations()[migration].down()

    @staticmethod
    def getDescriptionForAllMigrations():
        for migration in DbManager.getMigrations():
            DbManager.getMigrations()[migration].getDescription()

    @staticmethod
    def fillGroups():
        UniversityModel({'university_name': 'МЭИ'}).set()
        UniversityModel({'university_name': 'МГТУ'}).set()

    @staticmethod
    def resetDb():
        DbManager.downAllMigrations()
        DbManager.upAllMigrations()
        DbManager.fillGroups()
