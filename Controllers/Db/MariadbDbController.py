import mariadb

from Controllers.Db.AbstractSqlController import AbstractSqlController


class MariadbDbController(AbstractSqlController):

    def __init__(self):
        super().__init__()
        self.DB_PARAMS = {
            'user': self.config.MARIA_USERNAME,
            'password': self.config.MARIA_PASSWORD,
            'host': self.config.MARIA_HOST,
            'port': self.config.MARIA_PORT,
            'dbname': self.config.MARIA_DB,
            'connect_timeout': self.config.MARIA_CONN_TIMEOUT
        }
        self.conn = mariadb.connect(**self.DB_PARAMS)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """Closes cursor and conn connections when object destroys"""
        self.cursor.close()
        self.conn.close()
