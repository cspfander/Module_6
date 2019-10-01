"""
Program: inner_functions_assignment.py
Author: Colten Pfander
Last date modified: 9/30/2019

The purpose of this program is to write a function that accepts a list of measurements for a rectangle and returns a
string with perimeter and area.
"""


def measurements(measurement_list):
    def area(a_list):  # calculates the area
        if len(a_list) == 1:
            return a_list[0] * a_list[0]
        if len(a_list) == 2:
            return a_list[0] * a_list[1]

    def perimeter(a_list):  # calculates the perimeter
        if len(a_list) == 1:
            return a_list[0] * 4
        if len(a_list) == 2:
            return (a_list[0] * 2) + (a_list[1] * 2)
    return "Perimeter = " + str(perimeter(measurement_list)) + " Area = " + str(area(measurement_list))


if __name__ == '__main__':
    print(measurements([2.1, 3.4]))
