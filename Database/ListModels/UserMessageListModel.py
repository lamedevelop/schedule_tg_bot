from Database.Models.UserMessageModel import UserMessageModel
from Database.ListModels.AbstractListModel import AbstractListModel


class UserMessageListModel(AbstractListModel):

    def getList(self, model_class=UserMessageModel):
        return super(UserMessageListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=UserMessageModel):
        return super(UserMessageListModel, self).getListByParams(params, model_class)

    def count(self, model_class=UserMessageModel):
        return super(UserMessageListModel, self).count(model_class)
