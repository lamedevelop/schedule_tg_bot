from Database.Models.DbModel import DbModel


class UniversityModel(DbModel):

    table_name = 'universities'

    primary_key = ['university_id']

    fields = {
        primary_key[0]: '',
        'university_name': '',
    }

    def get(self, primary_key):
        return super(UniversityModel, self).get(primary_key)

    def set(self):
        super(UniversityModel, self).set()

    def update(self, new_fields):
        super(UniversityModel, self).update(new_fields)
