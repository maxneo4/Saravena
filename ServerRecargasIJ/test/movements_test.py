import unittest
from business.movements import process_movement
from data_core.data_values import DataValues


class TestVariables:
    def __init__(self):
        self.data_values_client = DataValues('CLIENTE', key_name='CODIGO')
        self.data_values_provider = DataValues('PROVEEDOR', key_name='CODIGO')
        self.data_values_store = DataValues('TIENDA', 'CODIGO')
        self.client_code = '544222'
        self.client_code_immediate_pay = '2551212'
        self.client_code_not_immediate_pay = '544222'
        self.provider_code = '4555121'
        self.store_code = '001'


class MovementsTestCase(unittest.TestCase):
    def setUp(self):
        self.wn = TestVariables()

    def test_add_valor_defecto_verificado_false(self):
        # given
        json_data = {'valor': 2250, 'tipo_movimiento': 'consignacion_proveedor', 'codigo_proveedor': self.wn.provider_code}
        # when
        process_movement(json_data)
        # then
        self.assertEquals(json_data["verificado"], u'false')

    def test_add_valor_defecto_verificado_true(self):
        # given
        json_data = {'valor': 3250, 'tipo_movimiento': 'cobro', 'codigo_cliente': self.wn.client_code}
        # when
        process_movement(json_data)
        # then
        self.assertEquals(json_data["verificado"], 1)

    def test_not_modify_verificado_value(self):
        # given
        json_data = {'valor': 2000, 'tipo_movimiento': 'cobro', 'codigo_cliente': self.wn.client_code, 'verificado': False}
        # when
        process_movement(json_data)
        # then
        self.assertEquals(json_data["verificado"], False)

    def verify_factor_movement(self, json_data, asociate_code, data_values, multiply_factor, column_name):
        # given
        current_balance = data_values.to(column_name).get_value(asociate_code)
        expect_balance = current_balance + json_data['valor'] * multiply_factor
        # when
        process_movement(json_data)
        # then
        result_balance = data_values.to(column_name).get_value(asociate_code)
        self.assertEquals(expect_balance, result_balance)

    def test_factor_cliente_increase(self):
            self.verify_factor_movement(
                json_data={'valor': 1000, 'tipo_movimiento': 'cobro', 'codigo_cliente': self.wn.client_code},
                asociate_code=self.wn.client_code,
                data_values=self.wn.data_values_client,
                multiply_factor=1,
                column_name='SALDO')

    def test_factor_cliente_decrease(self):
        self.verify_factor_movement(
            json_data={'valor': 2000, 'tipo_movimiento': 'recarga_cliente', 'codigo_cliente': self.wn.client_code, 'codigo_proveedor': self.wn.provider_code},
            asociate_code=self.wn.client_code,
            data_values=self.wn.data_values_client,
            multiply_factor=-1,
            column_name='SALDO')

    def test_factor_proveedor_increase(self):
            self.verify_factor_movement(
                json_data={'valor': 2000, 'tipo_movimiento': 'consignacion_proveedor', 'codigo_proveedor': self.wn.provider_code},
                asociate_code=self.wn.provider_code,
                data_values=self.wn.data_values_provider,
                multiply_factor=1,
                column_name='SALDO')

    def test_factor_proveedor_decrease(self):
        self.verify_factor_movement(
            json_data={'valor': 5000, 'tipo_movimiento': 'recarga_publico', 'codigo_proveedor': self.wn.provider_code},
            asociate_code=self.wn.provider_code,
            data_values=self.wn.data_values_provider,
            multiply_factor=-1,
            column_name='SALDO')

    def test_recarga_cliente_with_imediate_pay_then_(self):
        self.verify_factor_movement(
            json_data={'valor': 50000, 'tipo_movimiento': 'recarga_cliente', 'codigo_cliente': self.wn.client_code_immediate_pay, 'codigo_proveedor': self.wn.provider_code},
            asociate_code=self.wn.client_code_immediate_pay,
            data_values=self.wn.data_values_client,
            multiply_factor=-.95,
            column_name='SALDO')

    def test_recarga_cliente_with_not_imediate_pay_then_(self):
        self.verify_factor_movement(
            json_data={'valor': 80000, 'tipo_movimiento': 'recarga_cliente', 'codigo_cliente': self.wn.client_code_not_immediate_pay, 'codigo_proveedor': self.wn.provider_code},
            asociate_code=self.wn.client_code_not_immediate_pay,
            data_values=self.wn.data_values_client,
            multiply_factor=.05,
            column_name='GANANCIA_PENDIENTE')

    def test_factor_tienda_increase(self):
        self.verify_factor_movement(
            json_data={'valor': 1000, 'tipo_movimiento': 'cobro', 'codigo_cliente': self.wn.client_code},
            asociate_code=self.wn.store_code,
            data_values=self.wn.data_values_store,
            multiply_factor=1,
            column_name='SALDO')

    def test_factor_tienda_decrease(self):
        self.verify_factor_movement(
            json_data={'valor': 200000, 'tipo_movimiento': 'nomina'},
            asociate_code=self.wn.store_code,
            data_values=self.wn.data_values_store,
            multiply_factor=-1,
            column_name='SALDO')

    def test_factor_pago_pendiente(self):
        self.verify_factor_movement(
            json_data={'valor': 5000, 'tipo_movimiento': 'pago_cliente', 'codigo_cliente': self.wn.client_code},
            asociate_code=self.wn.client_code,
            data_values=self.wn.data_values_client,
            multiply_factor=-1,
            column_name='GANANCIA_PENDIENTE')

if __name__ == '__main__':
    unittest.main()
