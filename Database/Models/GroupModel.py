from Database.Models.AbstractModel import AbstractModel
from Controllers.DateTimeController import DateTimeController


class GroupModel(AbstractModel):

    table_name = 'groups'

    primary_key = ['group_id']

    fields = {
        primary_key[0]: '',
        'group_name': '',
        'university_id': '',
        'schedule_text': '',
        'schedule_url': '',
        'update_date': ''
    }

    def get(self, primary_key):
        return super(GroupModel, self).get(primary_key)

    def set(self):
        self.fields['update_date'] = int(DateTimeController.getCurrTimestamp())
        return super(GroupModel, self).set()

    def update(self, new_fields):
        new_fields['update_date'] = int(DateTimeController.getCurrTimestamp())
        super(GroupModel, self).update(new_fields)
