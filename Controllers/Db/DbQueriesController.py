class DbQueriesController:
    """
    SQL queries controller

    Logic level that could be changed in case of
    using non-sql database management system
    """

    def getSelectQuery(self, subject: str, source: str):
        return "SELECT {} FROM {}".format(subject, source)

    def getSelectWithParamQuery(self, subject, source, paramName, value):
        return "SELECT {} FROM {} WHERE {}=\"{}\"".format(subject, source, paramName, value)

    # For inserting several fields
    # use optimised queries
    def getInsertQuery(self, destination: str, subject: str, value):
        return """INSERT INTO {}
                (\"{}\") 
                VALUES (\"{}\")
        """.format(
            destination,
            subject,
            value
        )

    def getUpdateQuery(self, destination: str, subject: str, value, condParam: str, condVal):
        return """UPDATE {}
                SET {}={}
                WHERE {}=\"{}\";
        """.format(
            destination,
            subject,
            value,
            condParam,
            condVal
        )

    def checkIfExist(self, source: str, subject: str, value):
        return "SELECT COUNT(1) FROM {} WHERE {}={}".format(source, subject, value)

    def getGroupIdQuery(self, group_name: str, university_id):
        return """SELECT grop_id 
                FROM groups 
                WHERE group_name=\"{}\"
                AND university_id=\"{}\"
        """.format(
            group_name,
            university_id
        )

    # Optimized queries
    def getUserInsertQuery(self, destination: str, userInfo: dict):
        return """INSERT INTO {}
                ('{}', '{}', '{}', '{}') 
                VALUES ('{}', '{}', '{}', '{}')
        """.format(
            destination,
            'user_id',
            'first_name',
            'last_name',
            'username',
            userInfo.get('user_id'),
            userInfo.get('first_name'),
            userInfo.get('last_name'),
            userInfo.get('username'),
        )

    def getGroupInsertQuery(self, groupInfo: dict):
        return """INSERT INTO groups
                ('{}', '{}', '{}', '{}') 
                VALUES ('{}', '{}', '{}', '{}')
        """.format(
            "group_name",
            "university_id",
            "schedule_text",
            "schedule_url",
            groupInfo.get('group_name'),
            groupInfo.get('university_id'),
            groupInfo.get('schedule_text'),
            groupInfo.get('schedule_url'),

        )

    def getMessageInsertQuery(self, user_id, message):
        return """INSERT INTO userMessages
                ('{}', '{}') 
                VALUES ('{}', '{}')
        """.format(
            "user_id",
            "message",
            user_id,
            message,
        )