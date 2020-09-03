class UserController:

    DEFAULT_STATUS = 0
    UNIVERSITY_CHOSEN = 1
    GROUP_CHOSEN = 2

    def __init__(self):
        self.CURR_STATUS = self.DEFAULT_STATUS