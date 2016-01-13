import data
import responses

def get_all():
    return data.get_json_data('SELECT * FROM MOVIMIENTO')

def insert(json_data):
    print json_data
    return responses.get_json_status({'success':True}, 200)


