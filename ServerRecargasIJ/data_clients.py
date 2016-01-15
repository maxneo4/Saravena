from data_core.data import get_json_data
from data_core.data_values import DataValues

data_values = DataValues('CLIENTE', 'SALDO', 'CODIGO')

def get_all():
    return get_json_data('SELECT * FROM CLIENTE')

def operate_balance(client_code, value_movement):
    data_values.operate_balance(client_code, value_movement)


