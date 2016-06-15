from data_core.data_values import DataValues

data_values = DataValues('TIENDA', 'CODIGO')

def get_balance():
    return data_values.to('SALDO').get_value('001')

def operate_balance(value):
    data_values.to('SALDO').operate_int_value('001', value)