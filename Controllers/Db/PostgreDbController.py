import psycopg2
import subprocess

from Controllers.Db.AbstractSqlController import AbstractSqlController


class PostgreDbController(AbstractSqlController):

    def __init__(self):
        super().__init__()
        self.DB_PARAMS = {
            'user': self.config.POSTGRES_USERNAME,
            'password': self.config.POSTGRES_PASSWORD,
            'host': self.config.POSTGRES_HOST,
            'port': self.config.POSTGRES_PORT,
            'dbname': self.config.POSTGRES_DB,
            'connect_timeout': self.config.POSTGRES_CONN_TIMEOUT
        }
        self.conn = psycopg2.connect(**self.DB_PARAMS)
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
            self.logger.alert(f'Error while connecting to POSTGRES db: {error}')
            print('Problem query: ', query)

    def fetchQuery(self, query: str) -> list:
        try:
            self._executeQuery(query)
            result = self._fetchResult()
            return result
        except Exception as error:
            self.logger.alert(f'Error while connecting to POSTGRES db: {error}')
            print('Problem query: ', query)

    def makeDump(self):
        # pg_dump --dbname=postgresql://postgres:secret@postgresql_domain:5432/database -f dump.sql
        try:
            process = subprocess.Popen(
                [
                    'pg_dump',
                    '--dbname=postgresql://{}:{}@{}:{}/{}'.format(
                        self.config.POSTGRES_USERNAME,
                        self.config.POSTGRES_PASSWORD,
                        self.config.POSTGRES_HOST,
                        self.config.POSTGRES_PORT,
                        self.config.POSTGRES_DB
                    ),
                    '-f', self.config.DUMP_FILENAME
                ],
                stdout=subprocess.PIPE
            )
            if process.returncode != 0:
                self.logger.alert(
                    f'Command failed. Return code : {process.returncode}')
        except Exception as e:
            self.logger.alert(f'Error while dumping POSTGRES db: {e}')
