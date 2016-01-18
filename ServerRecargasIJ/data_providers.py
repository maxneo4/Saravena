from data_core.data_values import DataValues

data_values_provider = DataValues('PROVEEDOR', 'CODIGO')

def get_all():
    return data_values_provider.get_all_json_data()

def get_percent(provider_code):
    return data_values_provider.to('PORCENTAJE').get_value(provider_code)

def operate_balance(provider_code, value_movement):
    data_values_provider.to('SALDO').operate_int_value(provider_code, value_movement)