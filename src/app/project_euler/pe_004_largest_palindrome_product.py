"""
Project Euler Problem 4: https://projecteuler.net/problem=4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

References:
    - https://en.wikipedia.org/wiki/Palindromic_number
"""

class LargestPalindromeProduct:

    def __init__(self, n: int = 998001):
        self.n = n

    def solution(self) -> int:
        """
        Returns the largest palindrome made from the product of two 3-digit
        numbers which is less than n.

        >>> LargestPalindromeProduct(20000).solution()
        19591
        >>> LargestPalindromeProduct(30000).solution()
        29992
        >>> LargestPalindromeProduct(40000).solution()
        39893
        >>> LargestPalindromeProduct(10000).solution()
        Traceback (most recent call last):
            ...
        ValueError: That number is larger than our acceptable range.
        """

        # fetches the next number
        for number in range(self.n - 1, 9999, -1):
            str_number = str(number)

            # checks whether 'str_number' is a palindrome.
            if str_number == str_number[::-1]:
                divisor = 999

                # if 'number' is a product of two 3-digit numbers
                # then number is the answer otherwise fetch next number.
                while divisor != 99:
                    if (number % divisor == 0) and (len(str(number // divisor)) == 3):
                        return number
                    divisor -= 1
        raise ValueError("That number is larger than our acceptable range.")

    def solution(self) -> int:
        """
        Solution to the problem of finding the largest palindrome made from the product of two 3-digit numbers which is less than n.
        """

        answer = 0
        for i in range(999, 99, -1):  # 3 digit numbers range from 999 down to 100
            for j in range(999, 99, -1):
                product_string = str(i * j)
                if product_string == product_string[::-1] and i * j < self.n:
                    answer = max(answer, i * j)
        return answer
