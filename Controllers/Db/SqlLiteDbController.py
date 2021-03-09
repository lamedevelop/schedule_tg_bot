import os
import sqlite3

from Controllers.Db.AbstractSqlController import AbstractSqlController


class SqlLiteDbController(AbstractSqlController):

    def __init__(self):
        super().__init__()
        self.DB_PARAMS = {
            'database': self.config.DB_FILENAME
        }

    def _openConnection(self):
        """Open connection and create cursor"""
        self.conn = sqlite3.connect(**self.DB_PARAMS)
        self.cursor = self.conn.cursor()

    def _closeConnection(self):
        """Closes cursor and conn connections when object destroys"""
        self.cursor.close()
        self.conn.close()

    def _executeQuery(self, query: str) -> int:
        """Executes SQL statement

        @param query SQL statement
        """
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.lastrowid

    def _fetchResult(self) -> list:
        """Fetches result from last executed SELECT statement

        @return List of rows from result table
        """
        rows = self.cursor.fetchall()
        return [row for row in rows]

    def submitQuery(self, query: str) -> int:
        """Executes INSERT or UPDATE statements

        @param query SQL statement
        """
        try:
            self._openConnection()
            record_id = self._executeQuery(query)
            self._closeConnection()
            return record_id
        except Exception as error:
            self.logger.alert(f'Error while connecting to SQLITE db: {error}')
            print('Problem query: ', query)

    def fetchQuery(self, query: str) -> list:
        """Executes SELECT query and returns result

        @param query SQL statement
        """
        try:
            self._openConnection()
            self._executeQuery(query)
            result = self._fetchResult()
            self._closeConnection()
            return result
        except Exception as error:
            self.logger.alert(f'Error while connecting to SQLITE db: {error}')
            print('Problem query: ', query)

    def makeDump(self):
        """Makes dump database"""
        try:
            self._openConnection()
            with open(self.config.DUMP_FILENAME, 'w') as file:
                for line in self.conn.iterdump():
                    file.write('%s\n' % line)
            self._closeConnection()
        except Exception as error:
            self.logger.alert(f'Error while dumping SQLITE db: {error}')

    def dropDb(self):
        """Removes database file(storage)"""
        try:
            os.remove(self.config.DB_FILENAME)
            self.logger.info('DB was deleted')
        except Exception as e:
            self.logger.alert('Error while deleting SQLITE db: {}'.format(e))

    def checkConnection(self):
        """Check db availability"""
        try:
            self._openConnection()
            self._closeConnection()
            return self.DB_AVAILABLE
        except Exception as e:
            return self.DB_UNAVAILABLE
