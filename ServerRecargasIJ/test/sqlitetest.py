# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import data_movements
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
    def test_sqlite(self):   
        #data_movements.insert('request.json')
        print 'jsonData'
        assert 1 != 4;
        #self.assertEqual(x, y, "Msg");
        con = sqlite3.connect("Recargas.db3")
        cur = con.cursor()
        cur.execute('INSERT INTO MOVIMIENTO(fecha, codigo_asociado) VALUES (?, ?)', ('2016-01-07', '500') )
        con.commit()
        con.close()
        
    def test_insertion(self):
        data.insert_json_data('INSERT INTO MOVIMIENTO(fecha, codigo_asociado) VALUES (?, ?)', ('2016-01-07', '840') )

if __name__ == '__main__':
    unittest.main()

