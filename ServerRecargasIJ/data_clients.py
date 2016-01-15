from data_core.data import get_json_data
from data_core.data_values import DataValues

data_values_balance = DataValues('CLIENTE', 'SALDO', 'CODIGO')
data_values_pending_pay = DataValues('CLIENTE', 'GANANCIA_PENDIENTE', 'CODIGO')
data_values_immediate_pay = DataValues('CLIENTE', 'GANANCIA_INMEDIATA', 'CODIGO')

def get_all():
    return get_json_data('SELECT * FROM CLIENTE')

def get_pending_pay(client_code):
    return data_values_pending_pay.get_value(client_code)

def is_immediate_pay_client(client_code):
    immediate_pay = data_values_immediate_pay.get_value(client_code)
    return True if immediate_pay == u'true' else False

def operate_balance(client_code, value_movement):
    data_values_balance.operate_int_value(client_code, value_movement)

def operate_pending_pay(client_code, value_movement):
    data_values_pending_pay.operate_int_value(client_code, value_movement)


