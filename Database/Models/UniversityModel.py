from Database.Models.AbstractModel import AbstractModel


class UniversityModel(AbstractModel):

    table_name = 'universities'

    primary_key = ['university_id']

    fields = {
        primary_key[0]: '',
        'university_name': '',
    }

    def get(self, primary_key):
        return super(UniversityModel, self).get(primary_key)

    def set(self):
        return super(UniversityModel, self).set()

    def update(self, new_fields):
        super(UniversityModel, self).update(new_fields)

    def getUniversityByName(self, university: str):
        fields = self.dbController.fetchQuery(
            f"""SELECT {", ".join(self.fields.keys())} 
                FROM {self.table_name} 
                WHERE university_name LIKE '%{university}%'"""
        )

        if len(fields) > 0 and len(fields[0]) == len(self.fields):
            for field in enumerate(self.fields):
                self.fields[field[1]] = fields[0][field[0]]

        return self
