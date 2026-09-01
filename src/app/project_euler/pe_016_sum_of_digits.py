"""
Problem 16: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

class SumOfDigits:

    def solution_one(self, power: int = 1000) -> int:
        """Returns the sum of the digits of the number 2^power.
        >>> SumOfDigits().solution_one(1000)
        1366
        >>> SumOfDigits().solution_one(50)
        76
        >>> SumOfDigits().solution_one(20)
        31
        >>> SumOfDigits().solution_one(15)
        26
        """
        num = 2**power
        string_num = str(num)
        list_num = list(string_num)
        sum_of_num = 0

        for i in list_num:
            sum_of_num += int(i)

        return sum_of_num

    def solution_two(self, power: int = 1000) -> int:
        """Returns the sum of the digits of the number 2^power.

        >>> SumOfDigits().solution_two(1000)
        1366
        >>> SumOfDigits().solution_two(50)
        76
        >>> SumOfDigits().solution_two(20)
        31
        >>> SumOfDigits().solution_two(15)
        26
        """
        n = 2**power
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
