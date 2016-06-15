import data_movements_type
import data_movements
import data_clients
import data_providers
import data_store

def set_default_verified(movement_data, movement_type):
    if 'verificado' not in movement_data:
        movement_data['verificado'] = movement_type['valor_defecto_verificado']

def calculate_factor_client(movement_data, movement_type):
    if not movement_type.get('factor_cliente') is None:
        data_clients.operate_balance(movement_data['codigo_cliente'],
                                     movement_data['valor'] * movement_type['factor_cliente'])

def calculate_factor_provider(movement_data, movement_type):
    if not movement_type.get('factor_proveedor') is None:
        data_providers.operate_balance(movement_data['codigo_proveedor'],
                                     movement_data['valor'] * movement_type['factor_proveedor'])

def calculate_factor_store(movement_data, movement_type):
    if not movement_type.get('factor_tienda') is None:
        data_store.operate_balance(movement_data['valor'] * movement_type['factor_tienda'])

def calculate_factor_pending_pay_client(movement_data, movement_type):
    if not movement_type.get('factor_pago_pendiente') is None:
        data_clients.operate_pending_pay(movement_data['codigo_cliente'],
                                     movement_data['valor'] * movement_type['factor_pago_pendiente'])

def calculate_factor_pending_pay(movement_data, movement_type):
    if not movement_type.get('factor_pago_pendiente_porcentaje') is None:
        percent = float(data_providers.get_percent(movement_data['codigo_proveedor']))/float(100)
        value = movement_data['valor']
        client_code = movement_data['codigo_cliente']
        if data_clients.is_immediate_pay_client(client_code):
            data_clients.operate_balance(client_code, value*percent)
        else:
            data_clients.operate_pending_pay(client_code, value*percent)


def process_movement(movement_data):
    movement_type = data_movements_type.get_movement_type_by_movement_data(movement_data)
    set_default_verified(movement_data, movement_type)
    calculate_factor_client(movement_data, movement_type)
    calculate_factor_provider(movement_data, movement_type)
    calculate_factor_pending_pay(movement_data, movement_type)
    calculate_factor_store(movement_data, movement_type)
    calculate_factor_pending_pay_client(movement_data, movement_type)
    return data_movements.insert(movement_data)