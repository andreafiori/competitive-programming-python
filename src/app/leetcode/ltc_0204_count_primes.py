"""
Count Primes | Leetcode 204 | https://leetcode.com/problems/count-primes/

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
"""

class CountPrimes:
    def solution(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True] * n
        for i in range(2, n):
            if i * i >= n:
                break
            if not is_prime[i]:
                continue
            for j in range(i * i, n, i):
                is_prime[j] = False
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count
