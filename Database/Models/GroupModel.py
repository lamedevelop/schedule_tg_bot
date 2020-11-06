from Database.Models.DbModel import DbModel


class GroupModel(DbModel):

    table_name = 'groups'

    primary_key = ['group_id']

    fields = {
        primary_key[0]: '',
        'group_name': '',
        'university_id': '',
        'schedule_text': '',
        'schedule_url' : '',
        'update_date': ''
    }

    def get(self, primary_key):
        return super(GroupModel, self).get(primary_key)

    def set(self):
        super(GroupModel, self).set()

    def update(self, new_fields):
        super(GroupModel, self).update(new_fields)