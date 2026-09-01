"""
Problem 36: Double-base palindromes | https://projecteuler.net/problem=36

The decimal number,   (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base  and base .

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from __future__ import annotations

class DoubleBasePalindromes:

    def is_palindrome(self, n: int | str) -> bool:
        """
        Return true if the input n is a palindrome.
        Otherwise return false. n can be an integer or a string.

        >>> DoubleBasePalindromes().is_palindrome(909)
        True
        >>> DoubleBasePalindromes().is_palindrome(908)
        False
        >>> DoubleBasePalindromes().is_palindrome('10101')
        True
        >>> DoubleBasePalindromes().is_palindrome('10111')
        False
        """
        n = str(n)
        return n == n[::-1]


    def solution(self, n: int = 1000000):
        """Return the sum of all numbers, less than n , which are palindromic in
        base 10 and base 2.

        >>> DoubleBasePalindromes().solution(1000000)
        872187
        >>> DoubleBasePalindromes().solution(500000)
        286602
        >>> DoubleBasePalindromes().solution(100000)
        286602
        >>> DoubleBasePalindromes().solution(1000)
        1772
        >>> DoubleBasePalindromes().solution(100)
        157
        >>> DoubleBasePalindromes().solution(10)
        25
        >>> DoubleBasePalindromes().solution(2)
        1
        >>> DoubleBasePalindromes().solution(1)
        0
        """
        total = 0

        for i in range(1, n):
            if self.is_palindrome(i) and self.is_palindrome(bin(i).split("b")[1]):
                total += i
        return total
