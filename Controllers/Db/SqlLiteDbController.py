import os
import sqlite3

from Controllers.Db.AbstractSqlController import AbstractSqlController


class SqlLiteDbController(AbstractSqlController):

    def __init__(self):
        super().__init__()
        self.DB_PARAMS = {
            'database': self.config.DB_FILENAME
        }
        self.conn = sqlite3.connect(**self.DB_PARAMS)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def _executeQuery(self, query: str) -> int:
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.lastrowid

    def _fetchResult(self) -> list:
        rows = self.cursor.fetchall()
        return [row for row in rows]

    def submitQuery(self, query: str) -> int:
        try:
            record_id = self._executeQuery(query)
            return record_id
        except Exception as error:
            self.logger.alert(f'Error while connecting to SQLITE db: {error}')
            print('Problem query: ', query)

    def fetchQuery(self, query: str) -> list:
        try:
            self._executeQuery(query)
            result = self._fetchResult()
            return result
        except Exception as error:
            self.logger.alert(f'Error while connecting to SQLITE db: {error}')
            print('Problem query: ', query)

    def makeDump(self):
        try:
            with open(self.config.DUMP_FILENAME, 'w') as file:
                for line in self.conn.iterdump():
                    file.write('%s\n' % line)
        except Exception as error:
            self.logger.alert(f'Error while dumping SQLITE db: {error}')

    def dropDb(self):
        try:
            os.remove(self.config.DB_FILENAME)
            self.logger.info('DB was deleted')
        except Exception as e:
            self.logger.alert('Error while deleting SQLITE db: {}'.format(e))
