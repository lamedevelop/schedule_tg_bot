from abc import ABC, abstractmethod

from Controllers.CliArgsController import CliArgsController
from Controllers.Log.LogController import LogController


class AbstractSqlController(ABC):

    DB_PARAMS: dict

    DB_AVAILABLE = True
    DB_UNAVAILABLE = False

    def __init__(self) -> None:
        self.config = CliArgsController().getConfig()
        self.logger = LogController()

    @abstractmethod
    def _openConnection(self) -> None: ...

    @abstractmethod
    def _closeConnection(self) -> None: ...

    @abstractmethod
    def submitQuery(self, query: str) -> int: ...

    @abstractmethod
    def fetchQuery(self, query: str) -> list: ...

    @abstractmethod
    def makeDump(self) -> None: ...
