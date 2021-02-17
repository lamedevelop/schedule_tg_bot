import mariadb

from Controllers.FileController import FileController
from Controllers.Db.AbstractSqlController import AbstractSqlController


class MariaDbController(AbstractSqlController):

    def __init__(self):
        super().__init__()
        self.DB_PARAMS = {
            'user': self.config.MARIA_USERNAME,
            'password': self.config.MARIA_PASSWORD,
            'host': self.config.MARIA_HOST,
            'port': int(self.config.MARIA_PORT),
            'database': self.config.MARIA_DB,
            'connect_timeout': self.config.MARIA_CONN_TIMEOUT
        }

    def _openConnection(self):
        """Open connection and create cursor"""
        self.conn = mariadb.connect(**self.DB_PARAMS)
        self.cursor = self.conn.cursor()

    def _closeConnection(self):
        """Closes cursor and conn connections when object destroys"""
        self.cursor.close()
        self.conn.close()

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

            self.cursor.execute(query)
            record_id = self.cursor.lastrowid
            self.conn.commit()

            self._closeConnection()
            return record_id
        except Exception as error:
            self.logger.alert(
                f'Error while connecting to mariadb: {error}')
            print('Problem query: ', query)

    def fetchQuery(self, query: str) -> list:
        """Executes SELECT query and returns list

        @param query SQL statement
        """
        try:
            self._openConnection()

            self.cursor.execute(query)
            result = self._fetchResult()

            self._closeConnection()
            return result
        except Exception as error:
            self.logger.alert(
                f'Error while connecting to mariadb: {error}')
            print('Problem query: ', query)

    def makeDump(self):
        """Makes dump database"""
        try:
            FileController.runCommand(
                'mysqldump' +
                ' -h' + self.config.MARIA_HOST +
                ' -P' + self.config.MARIA_PORT +
                ' -u' + self.config.MARIA_USERNAME +
                ' --password=' + self.config.MARIA_PASSWORD +
                ' ' + self.config.MARIA_DB +
                ' >> ' + self.config.DUMP_FILENAME
            )
        except Exception as e:
            self.logger.alert(f'Error while dumping mariaDB: {e}')

    def connectToDb(self):
        """Command to connect to db from cli"""
        try:
            FileController.runCommand(
                f'mysql' +
                f' --host={self.config.MARIA_HOST}' +
                f' --port={int(self.config.MARIA_PORT)}'
                f' --user={self.config.MARIA_USERNAME}' +
                f' --password={self.config.MARIA_PASSWORD}'
            )
        except Exception as e:
            self.logger.alert(f'Error while connecting to mariaDB: {e}')

    def checkConnection(self):
        """Check db availability"""
        try:
            self._openConnection()
            self._closeConnection()
            return self.DB_AVAILABLE
        except Exception as e:
            return self.DB_UNAVAILABLE
