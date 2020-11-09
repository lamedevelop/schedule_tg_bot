from Database.ListModels.DbListModel import DbListModel
from Database.Models.UniversityModel import UniversityModel


class UniversityListModel(DbListModel):

    def getList(self, model_class=UniversityModel):
        return super(UniversityListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=UniversityModel):
        return super(UniversityListModel, self).getListByParams(params, model_class)
