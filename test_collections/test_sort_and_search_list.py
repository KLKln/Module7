import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list

class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list.search_list', return_value='4')
    def test_for_item_found(self, input):
        with self.assertEqual('4'):
            sort_and_search_list.search_list()

    @patch('fun_with_collections.sort_and_search_list.search_list', return_value='-1')
    def test_for_item_not_found(self, input):
        with self.assertEqual('-1'):
            sort_and_search_list.search_list()


if __name__ == '__main__':
    unittest.main()
