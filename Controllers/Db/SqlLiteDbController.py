from typing import overload
from Controllers.Db.AbstractDbController import AbstractDbController

import os
import sqlite3


class SqlLiteDbController(AbstractDbController):

    def __init__(self):
        super().__init__()
        self.DB_MODULE = sqlite3
        self.DB_PARAMS = {
            'database': self.config.DB_FILENAME
        }

    def makeDump(self):
        try:
            self._openConnection()
            with open(self.config.DUMP_FILENAME, 'w') as file:
                for line in self.conn.iterdump():
                    file.write('%s\n' % line)
            self._closeConnection()
        except Exception as error:
            self.logger.alert(f'Error while dumping db: {error}')

    def dropDb(self):
        try:
            os.remove(self.config.DB_FILENAME)
            self.logger.info('DB was deleted')
        except Exception as e:
            self.logger.alert('Error while deleting db: {}'.format(e))
