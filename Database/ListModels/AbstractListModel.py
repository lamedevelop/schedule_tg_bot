from Controllers.Db.DbFactoryController import DbFactoryController


class AbstractListModel:

    def __init__(self):
        self.dbController = DbFactoryController.getDbController()

    def getList(self, model_class):
        models = []

        records = self.dbController.fetchQuery(
            f'''SELECT {", ".join(model_class.fields.keys())} 
                FROM {model_class.table_name}'''
        )

        for record in records:
            record_dict = {
                key: record[index]
                for index, key in enumerate(model_class.fields)
            }

            models.append(model_class(record_dict))

        return models

    def getListByParams(self, params, model_class):
        query_params = []
        for key in params:
            query_params.append(key + "='" + str(params[key]) + "'")

        fields = self.dbController.fetchQuery(
            f'''SELECT {", ".join(model_class.fields.keys())} 
                FROM {model_class.table_name} 
                WHERE ''' + ' AND '.join(query_params)
        )

        return fields
