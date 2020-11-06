from abc import ABC, abstractmethod, abstractproperty


class DbModel(ABC):

    table_name = ''

    primary_key = ['']

    fields = {
        primary_key[0]: int
    }

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self):
        pass

    @abstractmethod
    def update(self):
        pass