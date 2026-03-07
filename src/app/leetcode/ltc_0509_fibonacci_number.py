"""
Fibonacci Number | https://leetcode.com/problems/fibonacci-number/description/
"""

class FibonacciNumber:

    def __init__(self):
        self.memo = []
        self.memo.append(0)
        self.memo.append(1)

    def fib(self, N: int) -> int:
        """
        DP with memo
        :type N: int
        :rtype: int
        """
        if N < len(self.memo):
            return self.memo[N]
        for i in range(len(self.memo), N + 1):
            self.memo.append(self.memo[i - 1] + self.memo[i - 2])
        return self.memo[N]
