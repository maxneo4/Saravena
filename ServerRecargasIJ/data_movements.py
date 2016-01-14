import data
import time

def get_all():
    return data.get_json_data('SELECT * FROM MOVIMIENTO')

def insert(json_data):
    return data.insert_json_data('INSERT INTO MOVIMIENTO(fecha, valor, tipo_movimiento, verificado, codigo_asociado) VALUES (?, ?, ?, ?, ?)', 
    (time.strftime("%Y-%m-%d"), json_data["valor"], json_data["tipo_movimiento"], json_data["verificado"], json_data["codigo_asociado"]) )