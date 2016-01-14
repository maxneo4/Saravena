import unittest
import data_clients

class SqliteTestCase(unittest.TestCase):

    def test_operate_balance(self):
        data_clients.operate_balance('2551212', 250)

if __name__ == '__main__':
    unittest.main()

