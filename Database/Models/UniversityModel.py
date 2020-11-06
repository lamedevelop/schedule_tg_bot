from Database.Models.DbModel import DbModel


class UniversityModel(DbModel):

    table_name = 'universities'

    primary_key = ['']

    fields = {
        primary_key[0]: int
    }

    def __init__(self):
        super().__init__()

    def get(self):
        pass

    def set(self):
        pass

    def update(self):
        pass