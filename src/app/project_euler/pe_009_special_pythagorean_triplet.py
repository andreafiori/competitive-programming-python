"""
Project Euler Problem 9: https://projecteuler.net/problem=9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.

References:
    - https://en.wikipedia.org/wiki/Pythagorean_triple
"""


class SpecialPythagoreanTriplet:

    def solution(self) -> int:
        """
        Returns the product of a,b,c which are Pythagorean Triplet that satisfies
        the following:
            1. a < b < c
            2. a**2 + b**2 = c**2
            3. a + b + c = 1000

        >>> SpecialPythagoreanTriplet().solution()
        31875000
        """

        for a in range(300):
            for b in range(a + 1, 400):
                for c in range(b + 1, 500):
                    if (a + b + c) == 1000 and (a**2) + (b**2) == (c**2):
                        return a * b * c

        return -1


    def solution_fast(self) -> int:
        """
        Returns the product of a,b,c which are Pythagorean Triplet that satisfies
        the following:
            1. a < b < c
            2. a**2 + b**2 = c**2
            3. a + b + c = 1000

        >>> SpecialPythagoreanTriplet().solution_fast()
        31875000
        """

        for a in range(300):
            for b in range(400):
                c = 1000 - a - b
                if a < b < c and (a**2) + (b**2) == (c**2):
                    return a * b * c

        return -1


    def benchmark(self) -> None:
        """
        Benchmark code comparing two different version function.
        """
        import timeit

        print(
            timeit.timeit("SpecialPythagoreanTriplet().solution()", setup="from __main__ import SpecialPythagoreanTriplet", number=1000)
        )
        print(
            timeit.timeit(
                "SpecialPythagoreanTriplet().solution_fast()", setup="from __main__ import SpecialPythagoreanTriplet", number=1000
            )
        )
