"""
Project Euler Problem 6: https://projecteuler.net/problem=6

Sum square difference

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

class SumSquareDifference:

    def __init__(self, n: int = 100):
        self.n = n


    def solution_one(self) -> int:
        """
        Returns the difference between the sum of the squares of the first n
        natural numbers and the square of the sum.

        >>> SumSquareDifference(10).solution_one()
        2640
        >>> SumSquareDifference(15).solution_one()
        13160
        >>> SumSquareDifference(20).solution_one()
        41230
        >>> SumSquareDifference(50).solution_one()
        1582700
        """

        sum_of_squares = 0
        sum_of_ints = 0
        for i in range(1, self.n + 1):
            sum_of_squares += i**2
            sum_of_ints += i
        return sum_of_ints**2 - sum_of_squares

    def solution_two(self) -> int:
        """
        Solution using the formula for the sum of the first n natural numbers and the sum of the squares of the first n natural numbers.
        """

        sum_cubes = (self.n * (self.n + 1) // 2) ** 2
        sum_squares = self.n * (self.n + 1) * (2 * self.n + 1) // 6
        return sum_cubes - sum_squares
