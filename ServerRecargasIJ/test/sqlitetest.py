# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import data_clients
import data

import sqlite3
import datetime

class  SqliteTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = Sqlite()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None
    def test_operate_balance(self):
        #data_movements.insert('request.json')
        print 'jsonData'
        data_clients.operate_balance('2551212', 250)
        
    def test_insertion(self):
        data.insert_json_data('INSERT INTO MOVIMIENTO(fecha, codigo_asociado) VALUES (?, ?)', ('2016-01-07', '840') )

if __name__ == '__main__':
    unittest.main()

