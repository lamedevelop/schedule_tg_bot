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