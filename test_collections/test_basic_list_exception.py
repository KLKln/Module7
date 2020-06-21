import unittest
from unittest.mock import patch
from fun_with_collections import basic_list_exception


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):                             # this is familiar
            basic_list_exception.make_list()                                          # call the function!



if __name__ == '__main__':
    unittest.main()
