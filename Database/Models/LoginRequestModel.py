from Database.Models.AbstractModel import AbstractModel
from Controllers.DateTimeController import DateTimeController


class LoginRequestModel(AbstractModel):

    table_name = 'loginRequests'

    primary_key = ['request_id']

    fields = {
        primary_key[0]: '',
        'group_id': '',
        'university_id': '',
        'client_ip': '',
        'update_date': 0
    }

    def get(self, primary_key):
        return super(LoginRequestModel, self).get(primary_key)

    def set(self):
        self.fields['update_date'] = int(DateTimeController.getCurrTimestamp())
        return super(LoginRequestModel, self).set()

    def update(self, new_fields):
        new_fields['update_date'] = int(DateTimeController.getCurrTimestamp())
        super(LoginRequestModel, self).update(new_fields)

    def drop(self):
        super(LoginRequestModel, self).drop()

    def getRequestByClient(self, client_ip: str):
        fields = self.dbController.fetchQuery(
            f"""SELECT {", ".join(self.fields.keys())} 
                        FROM {self.table_name} 
                        WHERE client_ip LIKE '%{client_ip}%'"""
        )

        if len(fields) > 0 and len(fields[0]) == len(self.fields):
            for field in enumerate(self.fields):
                self.fields[field[1]] = fields[0][field[0]]

        return self

