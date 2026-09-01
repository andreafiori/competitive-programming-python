"""
Problem 77: Prime Summations | https://projecteuler.net/problem=77

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""

from functools import lru_cache
from math import ceil

class PrimeSummations:

    NUM_PRIMES = 100

    primes = set(range(3, NUM_PRIMES, 2))
    primes.add(2)
    prime: int

    for prime in range(3, ceil(NUM_PRIMES**0.5), 2):
        if prime not in primes:
            continue
        primes.difference_update(set(range(prime * prime, NUM_PRIMES, prime)))

    @lru_cache(maxsize=100)
    def partition(self, number_to_partition: int) -> set[int]:
        """
        Return a set of integers corresponding to unique prime partitions of number_to_partition.
        The unique prime partitions can be represented as unique prime decompositions,
        e.g. (7+3) <-> 7*3 = 12, (3+3+2+2) = 3*3*2*2 = 36
        >>> PrimeSummations().partition(10)
        {32, 36, 21, 25, 30}
        >>> PrimeSummations().partition(15)
        {192, 160, 105, 44, 112, 243, 180, 150, 216, 26, 125, 126}
        >>> len(PrimeSummations().partition(20))
        26
        """
        if number_to_partition < 0:
            return set()
        elif number_to_partition == 0:
            return {1}

        ret: set[int] = set()
        prime: int
        sub: int

        for prime in self.primes:
            if prime > number_to_partition:
                continue
            for sub in self.partition(number_to_partition - prime):
                ret.add(sub * prime)

        return ret


    def solution(self, number_unique_partitions: int = 5000) -> int | None:
        """
        Return the smallest integer that can be written as the sum of primes in over
        number_unique_partitions unique ways.
        >>> PrimeSummations().solution(4)
        10
        >>> PrimeSummations().solution(500)
        45
        >>> PrimeSummations().solution(1000)
        53
        """
        for number_to_partition in range(1, self.NUM_PRIMES):
            if len(self.partition(number_to_partition)) > number_unique_partitions:
                return number_to_partition
        return None
