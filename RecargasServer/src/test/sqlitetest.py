# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import data

class  SqliteTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = Sqlite()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_sqlite(self):   
        data.get_users()
        assert 1 != 4;
        #self.assertEqual(x, y, "Msg");
        

if __name__ == '__main__':
    unittest.main()

