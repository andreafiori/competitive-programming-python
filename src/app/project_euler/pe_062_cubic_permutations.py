"""
Problem 62: Cubic permutations | https://projecteuler.net/problem=62

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""

from collections import defaultdict

class CubicPermutations:

    def solution(self, max_base: int = 5) -> int:
        """
        Iterate through every possible cube and sort the cube's digits in
        ascending order. Sorting maintains an ordering of the digits that allows
        you to compare permutations. Store each sorted sequence of digits in a
        dictionary, whose key is the sequence of digits and value is a list of
        numbers that are the base of the cube.

        Once you find 5 numbers that produce the same sequence of digits, return
        the smallest one, which is at index 0 since we insert each base number in
        ascending order.

        >>> CubicPermutations().solution(2)
        125
        >>> CubicPermutations().solution(3)
        41063625
        """
        freqs = defaultdict(list)
        num = 0

        while True:
            digits = self.get_digits(num)
            freqs[digits].append(num)

            if len(freqs[digits]) == max_base:
                base = freqs[digits][0] ** 3
                return base

            num += 1


    def get_digits(self, num: int) -> str:
        """
        Computes the sorted sequence of digits of the cube of num.

        >>> self.get_digits(3)
        '27'
        >>> self.get_digits(99)
        '027999'
        >>> self.get_digits(123)
        '0166788'
        """
        return "".join(sorted(str(num**3)))
