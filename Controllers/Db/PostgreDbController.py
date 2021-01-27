import psycopg2
import subprocess

from Controllers.Db.AbstractDbController import AbstractDbController


class PostgreDbController(AbstractDbController):

    def __init__(self):
        super().__init__()
        self.DB_MODULE = psycopg2
        self.DB_PARAMS = {
            'user': self.config.POSTGRES_USERNAME,
            'password': self.config.POSTGRES_PASSWORD,
            'host': self.config.POSTGRES_HOST,
            'port': self.config.POSTGRES_PORT,
            'dbname': self.config.POSTGRES_DB,
            'connect_timeout': self.config.POSTGRES_CONN_TIMEOUT
        }

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
            self.logger.alert(f'Error while dumping db: {e}')
