from Database.Models.GroupModel import GroupModel
from Controllers.DateTimeController import DateTimeController
from Controllers.SqlLiteDbController import SqlLiteDbController
from Database.ListModels.AbstractListModel import AbstractListModel


class GroupListModel(AbstractListModel):

    def getList(self, model_class=GroupModel):
        return super(GroupListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=GroupModel):
        return super(GroupListModel, self).getListByParams(params, model_class)

    def getListByDate(self, days_ago=7, model_class=GroupModel):

        time_deadline = DateTimeController.getPastTimestamp(days_ago)

        records = SqlLiteDbController().fetchQuery(
            f'''SELECT {", ".join(GroupModel.fields.keys())}
                FROM groups
                WHERE update_date<{time_deadline}'''
        )

        return self.getModelsList(records, model_class)

    def count(self, model_class=GroupModel):
        return super(GroupListModel, self).count(model_class)
