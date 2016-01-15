from data_core.data import get_json_data, insert_json_data
import time

def get_all():
    return get_json_data('SELECT * FROM MOVIMIENTO')

def insert(movement):
    verificado = movement.get('verificado', False)
    codigo_cliente = movement.get('codigo_cliente')
    codigo_proveedor = movement.get('codigo_proveedor')
    return insert_json_data('INSERT INTO MOVIMIENTO(fecha, valor, tipo_movimiento, verificado, codigo_cliente, codigo_proveedor) VALUES (?, ?, ?, ?, ?, ?)',
    (time.strftime("%Y-%m-%d"), movement["valor"], movement["tipo_movimiento"], verificado, codigo_cliente, codigo_proveedor) )