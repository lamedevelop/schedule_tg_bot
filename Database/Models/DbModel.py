from Controllers.Db.SqlLiteDbController import SqlLiteDbController


class DbModel:

    table_name = ''

    primary_key = ['']

    fields = {
        primary_key[0]: ''
    }

    def __init__(self, fields={}):
        for field_name in fields:
            if field_name in self.fields:
                self.fields[field_name] = fields[field_name]

        # Just a costyl, but without this line
        # new objects will rewrite old objects
        self.fields = self.fields.copy()

    def __repr__(self):
        self_fields = []
        for field_name in self.fields:
            self_fields.append(str(field_name) + ' = ' + str(self.fields[field_name]))
        return f'Object <{self.__class__.__name__}> with fields:\n> ' + \
               '\n> '.join(self_fields)

    def get(self, primary_key):
        fields = SqlLiteDbController().fetchQuery(
            f'''SELECT {", ".join(self.fields.keys())} 
                FROM {self.table_name} 
                WHERE {self.primary_key[0]}="{primary_key}"'''
        )

        if len(fields) > 0 and len(fields[0]) == len(self.fields):
            for field in enumerate(self.fields):
                self.fields[field[1]] = fields[0][field[0]]

        return self

    def set(self):
        set_fields = {
            'names': [],
            'values': []
        }
        for field_name in self.fields:
            if field_name != self.primary_key[0]:
                set_fields['names'].append(field_name)
                set_fields['values'].append('\"' + str(self.fields[field_name]) + '\"')

        SqlLiteDbController().submitQuery(
            f'''INSERT INTO {self.table_name} ({', '.join(set_fields['names'])}) 
                VALUES ({', '.join(set_fields['values'])})'''
        )

    def update(self, new_fields):
        update_fields = []

        for field_name in new_fields:
            if field_name in self.fields:
                self.fields[field_name] = new_fields[field_name]
                update_fields.append(field_name + '=\"' + str(new_fields[field_name]) + '\"')

        SqlLiteDbController().submitQuery(
            f'''UPDATE {self.table_name}
                SET {', '.join(update_fields)}
                WHERE {self.primary_key[0]}="{self.fields[self.primary_key[0]]}"'''
        )
