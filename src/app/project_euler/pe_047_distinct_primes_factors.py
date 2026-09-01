"""
Problem 47: Distinct Primes Factors | https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

from functools import lru_cache

class DistinctPrimesFactors:

    def unique_prime_factors(self, n: int) -> set:
        """
        Find unique prime factors of an integer.
        Tests include sorting because only the set matters,
        not the order in which it is produced.
        >>> sorted(set(DistinctPrimesFactors().unique_prime_factors(14)))
        [2, 7]
        >>> sorted(set(DistinctPrimesFactors().unique_prime_factors(644)))
        [2, 7, 23]
        >>> sorted(set(DistinctPrimesFactors().unique_prime_factors(646)))
        [2, 17, 19]
        """
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors


    @lru_cache
    def upf_len(self, num: int) -> int:
        """
        Memoize upf() length results for a given value.
        >>> DistinctPrimesFactors().upf_len(14)
        2
        """
        return len(self.unique_prime_factors(num))


    def equality(self, iterable: list) -> bool:
        """
        Check the equality of ALL elements in an iterable
        >>> DistinctPrimesFactors().equality([1, 2, 3, 4])
        False
        >>> DistinctPrimesFactors().equality([2, 2, 2, 2])
        True
        >>> DistinctPrimesFactors().equality([1, 2, 3, 2, 1])
        False
        """
        return len(set(iterable)) in (0, 1)


    def run(self, n: int) -> list[int]:
        """
        Runs core process to find problem solution.
        >>> DistinctPrimesFactors().run(3)
        [644, 645, 646]
        """

        # Incrementor variable for our group list comprehension.
        # This is the first number in each list of values
        # to test.
        base = 2

        while True:
            # Increment each value of a generated range
            group = [base + i for i in range(n)]

            # Run elements through the unique_prime_factors function
            # Append our target number to the end.
            checker = [self.upf_len(x) for x in group]
            checker.append(n)

            # If all numbers in the list are equal, return the group variable.
            if self.equality(checker):
                return group

            # Increment our base variable by 1
            base += 1


    def solution(self, n: int = 4) -> int | None:
        """Return the first value of the first four consecutive integers to have four
        distinct prime factors each.
        >>> DistinctPrimesFactors().solution()
        134043
        """
        results = self.run(n)
        return results[0] if len(results) else None
