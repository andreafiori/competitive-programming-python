"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

class MultiplesOf3And5:
    """
    Class to find the sum of all the multiples of 3 or 5 below a given number.
    """

    def __init__(self, n: int = 1000):
        self.n = n

    def solution_1(self) -> int:
        """
        Returns the sum of all the multiples of 3 or 5 below self.n.

        >>> MultiplesOf3And5(3).solution_1()
        0
        >>> MultiplesOf3And5(4).solution_1()
        3
        >>> MultiplesOf3And5(10).solution_1()
        23
        >>> MultiplesOf3And5(600).solution_1()
        83700
        >>> MultiplesOf3And5(-7).solution_1()
        0
        """

        return sum(e for e in range(3, self.n) if e % 3 == 0 or e % 5 == 0)

    def solution_2(self) -> int:
        """
        Solution using the formula for the sum of an arithmetic progression.
        """
        total = 0
        terms = (self.n - 1) // 3
        total += ((terms) * (6 + (terms - 1) * 3)) // 2  # total of an A.P.
        terms = (self.n - 1) // 5
        total += ((terms) * (10 + (terms - 1) * 5)) // 2
        terms = (self.n - 1) // 15
        total -= ((terms) * (30 + (terms - 1) * 15)) // 2
        return total

    def solution_3(self) -> int:
        """
        Solution using a while loop to iterate through all numbers below self.n and check if they are multiples of 3 or 5.
        """

        a = 3
        result = 0
        while a < self.n:
            if a % 3 == 0 or a % 5 == 0:
                result += a
            elif a % 15 == 0:
                result -= a
            a += 1
        return result

    def solution_4(self) -> int:
        """
        Solution using a for loop to iterate through all numbers below self.n and check if they are multiples of 3 or 5.
        """

        result = 0
        for i in range(self.n):
            if i % 3 == 0 or i % 5 == 0:
                result += i
        return result
