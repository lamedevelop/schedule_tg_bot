from Database.Models.TelegramUserModel import TelegramUserModel
from Database.ListModels.AbstractListModel import AbstractListModel


class TelegramUserListModel(AbstractListModel):

    def getList(self, model_class=TelegramUserModel):
        return super(TelegramUserListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=TelegramUserModel):
        return super(TelegramUserListModel, self).getListByParams(params, model_class)

    def count(self, model_class=TelegramUserModel):
        return super(TelegramUserListModel, self).count(model_class)
