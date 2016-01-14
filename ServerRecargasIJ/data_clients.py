import data

def get_all():
    return data.get_json_data('SELECT * FROM CLIENTE')

def operate_balance(client_code, value_movement):
    data_client = data.get_data('SELECT SALDO FROM CLIENTE WHERE CODIGO = ?', (client_code,))
    new_balance = data_client[0]["saldo"] + value_movement
    data.update_data("UPDATE CLIENTE SET SALDO = ? WHERE CODIGO = ?", (new_balance, client_code))


