from data_core.data import get_data

def get_movement_type_by_movement_data(movement_data):
    movements_type = get_data("SELECT * FROM TIPO_MOVIMIENTO WHERE TIPO_MOVIMIENTO = ?", (movement_data["tipo_movimiento"],))
    return movements_type[0]