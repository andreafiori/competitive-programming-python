"""
Problem 32: Pandigital products | https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

import itertools

class PandigitalProducts:

    def is_combination_valid(self, combination):
        """
        Checks if a combination (a tuple of 9 digits)
        is a valid product equation.

        >>> PandigitalProducts().is_combination_valid(('3', '9', '1', '8', '6', '7', '2', '5', '4'))
        True

        >>> PandigitalProducts().is_combination_valid(('1', '2', '3', '4', '5', '6', '7', '8', '9'))
        False

        """
        return (
            int("".join(combination[0:2])) * int("".join(combination[2:5]))
            == int("".join(combination[5:9]))
        ) or (
            int("".join(combination[0])) * int("".join(combination[1:5]))
            == int("".join(combination[5:9]))
        )


    def solution(self):
        """
        Finds the sum of all products whose multiplicand/multiplier/product identity
        can be written as a 1 through 9 pandigital

        >>> PandigitalProducts().solution()
        45228
        """

        return sum(
            {
                int("".join(pandigital[5:9]))
                for pandigital in itertools.permutations("123456789")
                if self.is_combination_valid(pandigital)
            }
        )
