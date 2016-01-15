import data


class DataValues:
    def __init__(self, table_name, column_name, key_name):
        self.table_name = table_name
        self.column_name = column_name
        self.key_name = key_name

    def operate_balance(self, key_value, value):
        data_client = data.get_data('SELECT {1} FROM {0} WHERE CODIGO = ?'.format(self.table_name, self.column_name),
                                    (key_value,))
        new_balance = data_client[0][self.column_name.lower()] + value
        data.update_data(
            "UPDATE {0} SET {1} = ? WHERE {2} = ?".format(self.table_name, self.column_name, self.key_name),
            (new_balance, key_value))
