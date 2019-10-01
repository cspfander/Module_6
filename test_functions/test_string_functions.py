import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        message = "Colten"
        n = 4
        self.assertEqual("ColtenColtenColtenColten", string_functions.multiply_string(message, n))


if __name__ == '__main__':
    unittest.main()
