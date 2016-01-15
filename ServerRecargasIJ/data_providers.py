from data_core.data import get_json_data, get_data, update_data
from data_core.data_values import DataValues

data_values = DataValues('PROVEEDOR', 'SALDO', 'CODIGO')

def get_all():
    return get_json_data('SELECT * FROM PROVEEDOR')

def operate_balance(provider_code, value_movement):
    data_values.operate_balance(provider_code, value_movement)