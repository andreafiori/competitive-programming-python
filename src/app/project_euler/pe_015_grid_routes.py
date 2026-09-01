"""
Problem 15: https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

from math import factorial

class GridRoutes:

    def solution(self, n: int = 20) -> int:
        """
        Returns the number of paths possible in a n x n grid starting at top left
        corner going to bottom right corner and being able to move right and down
        only.
        >>> GridRoutes().solution(25)
        126410606437752
        >>> GridRoutes().solution(23)
        8233430727600
        >>> GridRoutes().solution(20)
        137846528820
        >>> GridRoutes().solution(15)
        155117520
        >>> GridRoutes().solution(1)
        2
        """
        n = 2 * n  # middle entry of odd rows starting at row 3 is the solution for n = 1,
        # 2, 3,...
        k = n // 2

        return int(factorial(n) / (factorial(k) * factorial(n - k)))
