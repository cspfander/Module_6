"""
Program: validate_input_in_functions.py
Author: Colten Pfander
Last date modified: 9/30/2019

The purpose of this program is to write a function score_input() that takes a test_name, test_score, and
invalid_message that validates the test_score, asking the user for a valid test score until it is in the range,
then prints valid input as 'Test name: ##'.
"""


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    """
    :param test_name: stores user input as a test name to print
    :param test_score: stores a user input as a test score to print as well as be validated (optional)
    :param invalid_message: optional message that displays an indicated string if the user has input an invalid score
    :return: either returns a string with the Test_name : test_score or with an invalid_message for an invalid input
    """
    if 0 <= test_score <= 100:
        # return {test_name: test_score}
        return str(test_name) + ": " + str(test_score)
    else:
        return invalid_message


if __name__ == '__main__':
    print(score_input("Unit 9", 85))
