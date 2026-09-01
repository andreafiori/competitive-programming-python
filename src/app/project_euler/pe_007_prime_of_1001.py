"""
Project Euler Problem 7: https://projecteuler.net/problem=7

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

from math import sqrt

class PrimeOf10001s:

    def __init__(self, nth: int = 10001):
        self.nth = nth

    def solution(self) -> int:
        """
        Returns the n-th prime number.

        >>> PrimeOf10001s(6).solution()
        13
        >>> PrimeOf10001s(1).solution()
        2
        >>> PrimeOf10001s(3).solution()
        5
        >>> PrimeOf10001s(20).solution()
        71
        >>> PrimeOf10001s(50).solution()
        229
        >>> PrimeOf10001s(100).solution()
        541
        """

        count = 0
        number = 1
        while count != self.nth and number < 3:
            number += 1
            if self.is_prime(number):
                count += 1
        while count != self.nth:
            number += 2
            if self.is_prime(number):
                count += 1
        return number

    def solution_two(self) -> int:
        """
        Returns the n-th prime number.

        >>> PrimeOf10001s(6).solution_two()
        13
        >>> PrimeOf10001s(1).solution_two()
        2
        >>> PrimeOf10001s(3).solution_two()
        5
        >>> PrimeOf10001s(20).solution_two()
        71
        >>> PrimeOf10001s(50).solution_two()
        229
        >>> PrimeOf10001s(100).solution_two()
        541
        >>> PrimeOf10001s(3.4).solution_two()
        5
        >>> PrimeOf10001s(0).solution_two()
        Traceback (most recent call last):
            ...
        ValueError: Parameter nth must be greater than or equal to one.
        >>> PrimeOf10001s(-17).solution_two()
        Traceback (most recent call last):
            ...
        ValueError: Parameter nth must be greater than or equal to one.
        >>> PrimeOf10001s([]).solution_two()
        Traceback (most recent call last):
            ...
        TypeError: Parameter nth must be int or castable to int.
        >>> PrimeOf10001s("asd").solution_two()
        Traceback (most recent call last):
            ...
        TypeError: Parameter nth must be int or castable to int.
        """

        try:
            nth = int(self.nth)
        except (TypeError, ValueError):
            raise TypeError("Parameter nth must be int or castable to int.") from None
        if nth <= 0:
            raise ValueError("Parameter nth must be greater than or equal to one.")
        primes: list[int] = []
        num = 2
        while len(primes) < nth:
            if self.is_prime(num):
                primes.append(num)
                num += 1
            else:
                num += 1
        return primes[len(primes) - 1]

    def is_prime(self, number: int) -> bool:
        """Checks to see if a number is a prime in O(sqrt(n)).
        A number is prime if it has exactly two factors: 1 and itself.
        Returns boolean representing primality of given number (i.e., if the
        result is true, then the number is indeed prime else it is not).

        >>> PrimeOf10001s().is_prime(2)
        True
        >>> PrimeOf10001s().is_prime(3)
        True
        >>> PrimeOf10001s().is_prime(27)
        False
        >>> PrimeOf10001s().is_prime(2999)
        True
        >>> PrimeOf10001s().is_prime(0)
        False
        >>> PrimeOf10001s().is_prime(1)
        False
        """

        if 1 < number < 4:
            # 2 and 3 are primes
            return True
        elif number < 2 or number % 2 == 0 or number % 3 == 0:
            # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
            return False

        # All primes number are in format of 6k +/- 1
        for i in range(5, int(sqrt(number) + 1), 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False
        return True

    def prime_generator(self):
        """
        Generate a sequence of prime numbers
        """

        num = 2
        while True:
            if self.is_prime(num):
                yield num
            num += 1
