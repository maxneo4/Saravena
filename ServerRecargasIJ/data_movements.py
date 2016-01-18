from data_core.data import get_json_data, insert_json_data
from data_core.data_values import DataValues
import time

data_values_movement = DataValues('MOVIMIENTO', 'NUMERO')

def get_all():
    return data_values_movement.get_all_json_data()

def insert(movement):
    verificado = movement.get('verificado', False)
    codigo_cliente = movement.get('codigo_cliente')
    codigo_proveedor = movement.get('codigo_proveedor')
    return insert_json_data('INSERT INTO MOVIMIENTO(fecha, valor, tipo_movimiento, verificado, codigo_cliente, codigo_proveedor) VALUES (?, ?, ?, ?, ?, ?)',
    (time.strftime("%Y-%m-%d"), movement["valor"], movement["tipo_movimiento"], verificado, codigo_cliente, codigo_proveedor) )