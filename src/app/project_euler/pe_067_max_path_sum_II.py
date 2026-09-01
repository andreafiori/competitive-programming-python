"""
Problem 67: Maximum path sum II | https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.
"""

import os

class MaximumPathSumII:

    def solution_one(self):
        """
        Finds the maximum total in a triangle as described by the problem statement
        above.

        >>> MaximumPathSumII().solution_one()
        7273
        """
        script_dir = os.path.dirname(os.path.realpath(__file__)) + "/data"
        triangle = os.path.join(script_dir, "triangle.txt")

        with open(triangle) as f:
            triangle = f.readlines()

        a = []
        for line in triangle:
            numbers_from_line = []
            for number in line.strip().split(" "):
                numbers_from_line.append(int(number))
            a.append(numbers_from_line)

        for i in range(1, len(a)):
            for j in range(len(a[i])):
                number1 = a[i - 1][j] if j != len(a[i - 1]) else 0
                number2 = a[i - 1][j - 1] if j > 0 else 0
                a[i][j] += max(number1, number2)
        return max(a[-1])

    def solution_two(self) -> int:
        """
        Finds the maximum total in a triangle as described by the problem statement
        above.
        >>> MaximumPathSumII().solution_two()
        7273
        """
        script_dir = os.path.dirname(os.path.realpath(__file__)) + "/data"
        triangle_path = os.path.join(script_dir, "triangle.txt")

        with open(triangle_path) as in_file:
            triangle = [[int(i) for i in line.split()] for line in in_file]

        while len(triangle) != 1:
            last_row = triangle.pop()
            curr_row = triangle[-1]
            for j in range(len(last_row) - 1):
                curr_row[j] += max(last_row[j], last_row[j + 1])
        return triangle[0][0]