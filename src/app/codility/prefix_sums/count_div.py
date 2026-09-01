"""
CountDiv | https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

Compute number of integers divisible by k in range [a..b].

Write a function:
    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
    { i : A <= i <= B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three math divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:
        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A <= B.

Complexity:
        expected worst-case time complexity is O(1);
        expected worst-case space complexity is O(1).
"""

class CountDiv:
    def solution(self, a: int, b: int, k: int) -> int:
        """
        :param a: start integer
        :param b: end integer
        :param k: divisor integer
        :return: count of integers a..b divisible by k
        """
        # just depends whether A is part of the count itself, or not
        return b//k - a//k + 1 if a % k == 0 else b//k - a//k
