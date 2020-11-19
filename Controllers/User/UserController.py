from DbManager import DbManager
from MonitoringAlertManager import MonitoringAlertManager
from Controllers.Log.LogController import LogController


class UserController:

    DEFAULT_STATUS = 0
    UNIVERSITY_CHOSEN = 1
    GROUP_CHOSEN = 2

    DEFAULT_UNIVERSITY_ID = 0
    DEFAULT_GROUP_ID = 0

    # def __init__(self):
    #     self.CURR_STATUS = self.DEFAULT_STATUS

    def getCurrStatus(self, user_id):
        userInfo = DbManager.getTgUserInfo(user_id)

        if not userInfo:
            alert = f'UserController.getCurrStatus failed: user {user_id} info empty'
            LogController().alert(alert)
            MonitoringAlertManager().notify(alert, MonitoringAlertManager.WARNING_LEVEL)
            return self.DEFAULT_STATUS

        # if isinstance(userInfo['group_id'], int) and isinstance(userInfo['university_id'], int):
        if userInfo['group_id'] != '' and userInfo['university_id'] != '':
            return self.GROUP_CHOSEN
        # elif isinstance(userInfo['university_id'], int):
        elif userInfo['university_id'] != '':
            return self.UNIVERSITY_CHOSEN
        else:
            return self.DEFAULT_STATUS

    def getUserUniversityId(self, user_id):
        userInfo = DbManager.getTgUserInfo(user_id)

        if not userInfo:
            alert = f'UserController.getUserUniversityId failed: user {user_id} info empty'
            LogController().alert(alert)
            MonitoringAlertManager().notify(alert, MonitoringAlertManager.WARNING_LEVEL)
            return self.DEFAULT_UNIVERSITY_ID

        return userInfo['university_id']

    def getUserGroupId(self, user_id):
        userInfo = DbManager.getTgUserInfo(user_id)

        if not userInfo:
            alert = f'UserController.getUserGroupId failed: user {user_id} info empty'
            LogController().alert(alert)
            MonitoringAlertManager().notify(alert, MonitoringAlertManager.WARNING_LEVEL)
            return self.DEFAULT_GROUP_ID

        return userInfo['group_id']

    # @staticmethod
    # def getUserInfo(user_id):
    #     userInfo = DbManager().getTgUserInfo(user_id)
    #
    #     if not userInfo or len(userInfo) < 11:
    #         return []
    #
    #     return userInfo
