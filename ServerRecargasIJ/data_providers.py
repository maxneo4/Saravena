from data_core.data import get_json_data, get_data, update_data
from data_core.data_values import DataValues

data_values_saldo = DataValues('PROVEEDOR', 'SALDO', 'CODIGO')
data_values_percent = DataValues('PROVEEDOR', 'PORCENTAJE', 'CODIGO')

def get_all():
    return get_json_data('SELECT * FROM PROVEEDOR')

def get_percent(provider_code):
    return data_values_percent.get_value(provider_code)

def operate_balance(provider_code, value_movement):
    data_values_saldo.operate_int_value(provider_code, value_movement)