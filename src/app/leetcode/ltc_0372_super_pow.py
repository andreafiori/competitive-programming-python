"""
Super Pow | https://leetcode.com/problems/super-pow/
"""
class SuperPow:

    def __init__(self):
        self.base = 1337

    def pow(self, a: int, b: list[int]) -> int:
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # One knowledge: ab % k = (a%k)(b%k)%k
        # a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
        if b is None or len(b) == 0:
            return 1
        last_digit = b.pop()
        return self.powmod(self.pow(a, b), 10) * \
            self.powmod(a, last_digit) % self.base

    def powmod(self, a: int, k: int) -> int:
        a %= self.base
        result = 1
        for i in range(k):
            result = (result * a) % self.base
        return result
