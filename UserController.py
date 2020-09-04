from DbManager import DbManager


class UserController:

    DEFAULT_STATUS = 0
    UNIVERSITY_CHOSEN = 1
    GROUP_CHOSEN = 2

    def __init__(self):
        self.CURR_STATUS = self.DEFAULT_STATUS

    def getCurrStatus(self, user_id):
        userInfo = DbManager().getTgUserInfo(user_id)[0]

        if isinstance(userInfo[7], int) and isinstance(userInfo[8], int):
            return self.GROUP_CHOSEN
        elif isinstance(userInfo[7], int):
            return self.UNIVERSITY_CHOSEN
        else:
            return self.DEFAULT_STATUS

    def getUserUniversityId(self, user_id):
        userInfo = DbManager().getTgUserInfo(user_id)[0]
        return userInfo[7]

    def getUserGroupId(self, user_id):
        userInfo = DbManager().getTgUserInfo(user_id)[0]
        return userInfo[8]