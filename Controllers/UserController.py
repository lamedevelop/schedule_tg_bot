from DbManager import DbManager
from AlertManager import AlertManager

from Controllers.Log.LogController import LogController


class UserController:

    DEFAULT_STATUS = 0
    UNIVERSITY_CHOSEN = 1
    GROUP_CHOSEN = 2

    DEFAULT_GROUP_ID = 0
    DEFAULT_UNIVERSITY_ID = 0

    def getCurrStatus(self, user_id):
        userInfo = DbManager.getTgUserInfo(user_id)

        if not userInfo:
            alert = f'UserController.getCurrStatus failed: user {user_id} info empty'
            LogController().alert(alert)
            AlertManager().notify(alert, AlertManager.WARNING_LEVEL)
            return self.DEFAULT_STATUS

        if userInfo['group_id'] != self.DEFAULT_GROUP_ID \
                and userInfo['university_id'] != self.DEFAULT_UNIVERSITY_ID:
            return self.GROUP_CHOSEN

        elif userInfo['university_id'] != self.DEFAULT_UNIVERSITY_ID:
            return self.UNIVERSITY_CHOSEN

        else:
            return self.DEFAULT_STATUS

    def getUserUniversityId(self, user_id):
        userInfo = DbManager.getTgUserInfo(user_id)

        if not userInfo:
            alert = f'UserController.getUserUniversityId failed: user {user_id} info empty'
            LogController().alert(alert)
            AlertManager().notify(alert, AlertManager.WARNING_LEVEL)
            return self.DEFAULT_UNIVERSITY_ID

        return userInfo['university_id']

    def getUserGroupId(self, user_id):
        userInfo = DbManager.getTgUserInfo(user_id)

        if not userInfo:
            alert = f'UserController.getUserGroupId failed: user {user_id} info empty'
            LogController().alert(alert)
            AlertManager().notify(alert, AlertManager.WARNING_LEVEL)
            return self.DEFAULT_GROUP_ID

        return userInfo['group_id']
