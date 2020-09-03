class DbQueriesController:
    """
    SQL queries controller

    Logic level that could be changed in case of
    using non-sql database management system
    """

    def getSelectQuery(self, subject, source):
        return "SELECT {} FROM {}".format(subject, source)

    # For inserting several fields
    # use optimised queries
    def getInsertQuery(self, destination, subject, value):
        return """INSERT INTO {}
            (\"{}\") 
            VALUES (\"{}\")""".format(
            destination,
            subject,
            value
        )

    def checkIfExist(self, source, subject, value):
        return "SELECT COUNT(1) FROM {} WHERE {}={}".format(source, subject, value)

    def getUserInsertQuery(self, destination, userInfo):
        return """INSERT INTO {}
                    ('{}', '{}', '{}', '{}') 
                    VALUES ('{}', '{}', '{}', '{}')""".format(
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