"""
Fibonacci Number | leetcode 509 | https://leetcode.com/problems/fibonacci-number/
"""

class FibonacciNumber:

    def __init__(self):
        self.memo = []
        self.memo.append(0)
        self.memo.append(1)

    def fib(self, n: int) -> int:
        """
        DP with memo
        :type n: int
        :rtype: int
        """
        if n < len(self.memo):
            return self.memo[n]
        for i in range(len(self.memo), n + 1):
            self.memo.append(self.memo[i - 1] + self.memo[i - 2])
        return self.memo[n]
