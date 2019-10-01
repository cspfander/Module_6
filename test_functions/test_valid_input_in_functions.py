import unittest
from more_functions import validate_input_in_functions


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Unit 24: 0", validate_input_in_functions.score_input("Unit 24"))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Unit 12: 80", validate_input_in_functions.score_input("Unit 12", 80))

    def test_score_input_test_score_below_range(self):
        self.assertEqual("Invalid test score, try again!", validate_input_in_functions.score_input(("Unit 10", -1)))

    def test_score_input_test_score_above_range(self):
        self.assertEqual("Invalid test score, try again!", validate_input_in_functions.score_input(("Unit 9", 101)))

    def test_score_non_numeric(self):
        self.assertEqual("Invalid test score! Please use only numeric!", validate_input_in_functions.score_input("Unit 8", "i"))

    def test_score_input_invalid_message(self):
        self.assertEqual("YOU MESSED UP!", validate_input_in_functions.score_input("Unit 7", -20, "YOU MESSED UP!"))


if __name__ == '__main__':
    unittest.main()
