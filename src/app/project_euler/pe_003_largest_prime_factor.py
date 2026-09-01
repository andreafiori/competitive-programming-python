"""
Project Euler Problem 3: https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

References:
    - https://en.wikipedia.org/wiki/Prime_number#Unique_factorization
"""

import math

class LargestPrimeFactor:
    """Class to find the largest prime factor of a number."""

    def __init__(self, n: int = 600851475143):
        self.number = n

    def is_prime(self, number: int) -> bool:
        """Checks to see if a number is a prime in O(sqrt(n)).
        A number is prime if it has exactly two factors: 1 and itself.
        Returns boolean representing primality of given number (i.e., if the
        result is true, then the number is indeed prime else it is not).

        >>> PrimeNumber.is_prime(2)
        True
        >>> PrimeNumber.is_prime(3)
        True
        >>> PrimeNumber.is_prime(27)
        False
        >>> PrimeNumber.is_prime(2999)
        True
        >>> PrimeNumber.is_prime(0)
        False
        >>> PrimeNumber.is_prime(1)
        False
        """

        if 1 < number < 4:
            # 2 and 3 are primes
            return True
        elif number < 2 or number % 2 == 0 or number % 3 == 0:
            # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
            return False

        # All primes number are in format of 6k +/- 1
        for i in range(5, int(math.sqrt(number) + 1), 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False
        return True

    def solution_one(self) -> int:
        """
        Returns the largest prime factor of a given number n.

        >>> LargestPrimeFactor(13195).solution_one()
        29
        >>> LargestPrimeFactor(10).solution_one()
        5
        >>> LargestPrimeFactor(17).solution_one()
        17
        >>> LargestPrimeFactor(3.4).solution_one()
        3
        >>> LargestPrimeFactor(0).solution_one()
        Traceback (most recent call last):
            ...
        ValueError: Parameter n must be greater than or equal to one.
        >>> LargestPrimeFactor(-17).solution_one()
        Traceback (most recent call last):
            ...
        ValueError: Parameter n must be greater than or equal to one.
        >>> LargestPrimeFactor([]).solution_one()
        Traceback (most recent call last):
            ...
        TypeError: Parameter n must be int or castable to int.
        >>> LargestPrimeFactor("asd").solution_one()
        Traceback (most recent call last):
            ...
        TypeError: Parameter n must be int or castable to int.
        """

        try:
            n = int(self.number)
        except (TypeError, ValueError):
            raise TypeError("Parameter n must be int or castable to int.")
        if n <= 0:
            raise ValueError("Parameter n must be greater than or equal to one.")
        max_number = 0
        if self.is_prime(n):
            return n
        while n % 2 == 0:
            n //= 2
        if self.is_prime(n):
            return n
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                if self.is_prime(n // i):
                    max_number = n // i
                    break
                elif self.is_prime(i):
                    max_number = i
        return max_number
