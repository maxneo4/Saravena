from data_core.data_values import DataValues

data_values_client = DataValues('CLIENTE', 'CODIGO')

def get_all():
    return data_values_client.get_all_json_data()

def get_pending_pay(client_code):
    return data_values_client.to('GANANCIA_PENDIENTE').get_value(client_code)

def is_immediate_pay_client(client_code):
    immediate_pay = data_values_client.to('GANANCIA_INMEDIATA').get_value(client_code)
    return True if immediate_pay == u'true' else False

def operate_balance(client_code, value_movement):
    data_values_client.to('SALDO').operate_int_value(client_code, value_movement)

def operate_pending_pay(client_code, value_movement):
    data_values_client.to('GANANCIA_PENDIENTE').operate_int_value(client_code, value_movement)


