import unittest
from test_book import TestBook

if __name__ == "__main__":

# O lista cu numele testelor in ordinea dorita
 test_order = [
    'test_get_info',
    'test_is_in_stock_when_stock_is_negative',
    'test_is_in_stock_when_stock_is_positive',
    'test_is_in_stock_when_stock_is_zero',
    'test_update_stock',
    'test_update_stock_negative',
    'test_book_str_representation',
    'test_update_stock_zero',
    'test_update_stock_multiple_times',
    'test_update_stock_large_quantity'
]



test_suite = unittest.TestSuite()

for test_name in test_order:
    test_suite.addTest(TestBook(test_name))

if __name__ == "__main__":
    unittest.main()



