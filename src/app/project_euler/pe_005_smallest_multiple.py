"""
Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?

References:
    - https://en.wiktionary.org/wiki/evenly_divisible
    - https://en.wikipedia.org/wiki/Euclidean_algorithm
    - https://en.wikipedia.org/wiki/Least_common_multiple
"""

from math import gcd as greatest_common_divisor

class SmallestMultiple:

    def __init__(self, n: int = 20):
        self.n = n

    def solution_one(self) -> int:
        """
        Returns the smallest positive number that is evenly divisible (divisible
        with no remainder) by all of the numbers from 1 to n.

        >>> SmallestMultiple(10).solution()
        2520
        >>> SmallestMultiple(15).solution()
        360360
        >>> SmallestMultiple(22).solution()
        232792560
        >>> SmallestMultiple(3.4).solution()
        6
        >>> SmallestMultiple(0).solution()
        Traceback (most recent call last):
            ...
        ValueError: Parameter n must be greater than or equal to one.
        >>> SmallestMultiple(-17).solution()
        Traceback (most recent call last):
            ...
        ValueError: Parameter n must be greater than or equal to one.
        >>> SmallestMultiple([]).solution()
        Traceback (most recent call last):
            ...
        TypeError: Parameter n must be int or castable to int.
        >>> SmallestMultiple("asd").solution()
        Traceback (most recent call last):
            ...
        TypeError: Parameter n must be int or castable to int.
        """

        try:
            n = int(self.n)
        except (TypeError, ValueError):
            raise TypeError("Parameter n must be int or castable to int.")
        if n <= 0:
            raise ValueError("Parameter n must be greater than or equal to one.")
        i = 0
        while 1:
            i += n * (n - 1)
            nfound = 0
            for j in range(2, n):
                if i % j != 0:
                    nfound = 1
                    break
            if nfound == 0:
                if i == 0:
                    i = 1
                return i

    def least_common_multiple(self, x: int, y: int) -> int:
        """
        Least Common Multiple.
        """
        return (x * y) // greatest_common_divisor(x, y)

    def solution_two(self) -> int:
        """
        Returns the smallest positive number that is evenly divisible (divisible
        """

        g = 1
        for i in range(1, self.n + 1):
            g = self.least_common_multiple(g, i)
        return g
