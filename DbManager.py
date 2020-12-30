from Database.ListModels.TelegramUserListModel import TelegramUserListModel
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

from datetime import datetime

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

    logger = LogController()

    @staticmethod
    def run():
        print('empty method')

    @staticmethod
    def addUniversity(university_name: str):
        UniversityModel({'university_name': university_name}).set()

    @staticmethod
    def getUniversities():
        return [university.fields for university in UniversityListModel().getList()]

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
        from ParseManager import ParseManager
        groups = GroupListModel().getListByDate()
        for group_id, group_name, university_id in groups:
            new_schedule_text = ParseManager.downloadSchedule(
                university_id, group_name
            )
            GroupModel().get(group_id).update({
                'schedule_text': new_schedule_text,
                'update_date': f'{datetime.now().timestamp()}'
            })

    # Should be fixed before using
    # @staticmethod
    # def getGroupsByUniversityId(universityId):
    #     records = GroupListModel().getListByParams({'university_id': universityId})
    #     return [
    #         {
    #             'group_id': record.fields['group_id'],
    #             'group_name': record.fields['group_name'],
    #         } for record in records
    #     ]

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

    # Migrations methods
    @staticmethod
    def upMigration(migration):
        DbManager.migrations.get(migration).up()

    @staticmethod
    def downMigration(migration):
        DbManager.migrations.get(migration).down()

    @staticmethod
    def upAllMigrations():
        for migration in DbManager.migrations:
            DbManager.migrations[migration].up()

    @staticmethod
    def downAllMigrations():
        for migration in DbManager.migrations:
            DbManager.migrations[migration].down()

    @staticmethod
    def getDescriptionForAllMigrations():
        for migration in DbManager.migrations:
            DbManager.migrations[migration].getDescription()

    @staticmethod
    def fillGroups():
        UniversityModel({'university_name': 'МЭИ'}).set()
        UniversityModel({'university_name': 'МГТУ'}).set()

    @staticmethod
    def resetDb():
        DbManager.downAllMigrations()
        DbManager.upAllMigrations()
        DbManager.fillGroups()
