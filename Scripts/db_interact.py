"""
Script that provide interface for base functions of DbManager.
"""

from DbManager import DbManager
from Controllers.Log.LogController import LogController


def upMigration(dbManager, migration):
    dbManager.upMigration(migration)


def downMigration(dbManager, migration):
    dbManager.downMigration(migration)


def upAllMigrations(dbManager):
    dbManager.upAllMigrations()


def downAllMigrations(dbManager):
    dbManager.downAllMigrations()


def fillTestData(dbManager):
    dbManager.fillGroups()


def resetDb(dbManager):
    dbManager.resetDb()


def dropDb(dbManager):
    dbManager.dropDb()


# Currently this script creates base structure
# of tables in db and filling them with test data.
#
# If tables already exist and you want to
# reset the db file then change modifier
def main():
    dbManager = DbManager()
    logger = LogController()

    commands = {
        "setup_db"                          : 0,

        "upAllMigrations"                   : 1,
        "downAllMigrations"                 : 2,

        "upGroupsTableMigration"            : 3,
        "upUniversitiesTableMigration"      : 4,
        "upTelegramUsersTableMigration"     : 5,
        "upUserMessagesTableMigration"      : 6,

        "downGroupsTableMigration"          : 7,
        "downUniversitiesTableMigration"    : 8,
        "downTelegramUsersTableMigration"   : 9,
        "downUserMessagesTableMigration"    : 10,

        "resetDb"                           : 11,
    }

    # Change operation by changing requested
    # dict key in this line
    command_name = "setup_db"
    command_id = commands.get(command_name, 999)

    if command_id == 0:
        logger.info(f'db_interact script run with command {command_name}')
        upAllMigrations(dbManager)
        fillTestData(dbManager)

    elif command_id == 1:
        logger.info(f'db_interact script run with command {command_name}')
        upAllMigrations(dbManager)

    elif command_id == 2:
        logger.info(f'db_interact script run with command {command_name}')
        downAllMigrations(dbManager)

    elif command_id == 3:
        logger.info(f'db_interact script run with command {command_name}')
        upMigration(dbManager, "groupsTableMigration")

    elif command_id == 4:
        logger.info(f'db_interact script run with command {command_name}')
        upMigration(dbManager, "universitiesTableMigration")

    elif command_id == 5:
        logger.info(f'db_interact script run with command {command_name}')
        upMigration(dbManager, "telegramUsersTableMigration")

    elif command_id == 6:
        logger.info(f'db_interact script run with command {command_name}')
        upMigration(dbManager, "userMessagesTableMigration")

    elif command_id == 7:
        logger.info(f'db_interact script run with command {command_name}')
        downMigration(dbManager, "groupsTableMigration")

    elif command_id == 8:
        logger.info(f'db_interact script run with command {command_name}')
        downMigration(dbManager, "universitiesTableMigration")

    elif command_id == 9:
        logger.info(f'db_interact script run with command {command_name}')
        downMigration(dbManager, "telegramUsersTableMigration")

    elif command_id == 10:
        logger.info(f'db_interact script run with command {command_name}')
        downMigration(dbManager, "userMessagesTableMigration")

    elif command_id == 11:
        logger.info(f'db_interact script run with command {command_name}')
        resetDb(dbManager)

    else:
        logger.alert(f'db_interact script run with unrecognized command {command_name}')
