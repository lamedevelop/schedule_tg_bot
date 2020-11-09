from Database.ListModels.DbListModel import DbListModel
from Database.Models.GroupModel import GroupModel

from Controllers.Db.SqlLiteDbController import SqlLiteDbController
from Database.Models.UserMessageModel import UserMessageModel


class GroupListModel(DbListModel):

    def getList(self, model_class=UserMessageModel):
        return super(GroupListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=UserMessageModel):
        return super(GroupListModel, self).getListByParams(params, model_class)
