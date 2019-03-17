# coding: utf-8

import unittest
from domain import Column, DataTable

class DataTableTest(unittest.TestCase):
    def setUp(self):
        self.table = DataTable('A')

    def test_add_column(self):
        self.assertEqual(0, len(self.table._columns))
        
        self.table.add_column('BId', 'bigint')
        self.assertEqual(1, len(self.table._columns))

        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table._columns))

        self.table.add_column('desc', 'varchar')
        self.assertEqual(3, len(self.table._columns))
    
    def test_add_column_invalid_type(self):
        self.assertRaises(Exception, self.table.add_column, ('col', 'invalid'))

    def test_add_column_invalid_type_fail(self):
        error = False

        try:
            self.table.add_column('col', 'invalid')
        except:
            error = True

        if not error:
            self.fail('Chamada não gerou erro, mas deveria')

if __name__ == '__main__':
    unittest.main()