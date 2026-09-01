"""
Problem 48: Self Powers | https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

class SelfPowers:

    def solution(self) -> str:
        """
        Returns the last 10 digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

        >>> SelfPowers().solution()
        '9110846700'
        """
        total = 0
        for i in range(1, 1001):
            total += i**i
        return str(total)[-10:]
