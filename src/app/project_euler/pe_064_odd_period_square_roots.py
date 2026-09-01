"""
Problem 64: Odd period square roots | https://projecteuler.net/problem=64

All square roots are periodic when written as continued fractions.
For example, let us consider sqrt(23).
It can be seen that the sequence is repeating.
For conciseness, we use the notation sqrt(23)=[4;(1,3,1,8)],
to indicate that the block (1,3,1,8) repeats indefinitely.
Exactly four continued fractions, for N<=13, have an odd period.
How many continued fractions for N<=10000 have an odd period?

References: https://en.wikipedia.org/wiki/Continued_fraction
"""

from math import floor, sqrt

class OddPeriodSquareRoots:

    def continuous_fraction_period(self, n: int) -> int:
        """
        Returns the continued fraction period of a number n.

        >>> OddPeriodSquareRoots().continuous_fraction_period(2)
        1
        >>> OddPeriodSquareRoots().continuous_fraction_period(5)
        1
        >>> OddPeriodSquareRoots().continuous_fraction_period(7)
        4
        >>> OddPeriodSquareRoots().continuous_fraction_period(11)
        2
        >>> OddPeriodSquareRoots().continuous_fraction_period(13)
        5
        """
        numerator = 0.0
        denominator = 1.0
        root = int(sqrt(n))
        integer_part = root
        period = 0
        while integer_part != 2 * root:
            numerator = denominator * integer_part - numerator
            denominator = (n - numerator**2) / denominator
            integer_part = int((root + numerator) / denominator)
            period += 1
        return period


    def solution(self, n: int = 10000) -> int:
        """
        Returns the count of numbers <= 10000 with odd periods.
        This function calls continuous_fraction_period for numbers which are
        not perfect squares.
        This is checked in if sr - floor(sr) != 0 statement.
        If an odd period is returned by continuous_fraction_period,
        count_odd_periods is increased by 1.

        >>> OddPeriodSquareRoots().solution(2)
        1
        >>> OddPeriodSquareRoots().solution(5)
        2
        >>> OddPeriodSquareRoots().solution(7)
        2
        >>> OddPeriodSquareRoots().solution(11)
        3
        >>> OddPeriodSquareRoots().solution(13)
        4
        """
        count_odd_periods = 0
        for i in range(2, n + 1):
            sr = sqrt(i)
            if sr - floor(sr) != 0 and self.continuous_fraction_period(i) % 2 == 1:
                count_odd_periods += 1
        return count_odd_periods
