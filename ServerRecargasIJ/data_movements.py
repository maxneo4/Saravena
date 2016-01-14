import data
import time

def get_all():
    return data.get_json_data('SELECT * FROM MOVIMIENTO')

def insert(json_data):
    verificado = json_data['verificado'] if 'verificado' in json_data else False
    codigo_cliente = json_data['codigo_cliente'] if 'codigo_cliente' in json_data else None
    codigo_proveedor = json_data['codigo_proveedor'] if 'codigo_proveedor' in json_data else None
    return data.insert_json_data('INSERT INTO MOVIMIENTO(fecha, valor, tipo_movimiento, verificado, codigo_cliente, codigo_proveedor) VALUES (?, ?, ?, ?, ?, ?)',
    (time.strftime("%Y-%m-%d"), json_data["valor"], json_data["tipo_movimiento"], verificado, codigo_cliente, codigo_proveedor) )