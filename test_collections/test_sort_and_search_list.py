import unittest
from unittest import mock
from unittest.mock import patch
from fun_with_collections import sort_and_search_list

user_list = [21, 31, 56, 78, 22, 4, 13, 42, 9]


class MyTestCase(unittest.TestCase):
    def test_for_item_found(self):
        with mock.patch('builtins.input', return_value="your number is at index 0"):
            self.assertEqual("21", sort_and_search_list.search_list(user_list))

    def test_for_item_not_found(self):
        with mock.patch('builtins.input', return_value="-1"):
            self.assertEqual("41", sort_and_search_list.search_list(user_list))



if __name__ == '__main__':
    unittest.main()
