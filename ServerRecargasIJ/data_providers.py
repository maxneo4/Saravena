import data

def get_all():
    return data.get_json_data('SELECT * FROM PROVEEDOR')

def operate_balance(provider_code, value_movement):
    data_client = data.get_data('SELECT SALDO FROM PROVEEDOR WHERE CODIGO = ?', (provider_code,))
    new_balance = data_client[0]["saldo"] + value_movement
    data.update_data("UPDATE PROVEEDOR SET SALDO = ? WHERE CODIGO = ?", (new_balance, provider_code))
