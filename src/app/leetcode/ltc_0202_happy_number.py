"""
Happy Number | https://leetcode.com/problems/happy-number/description/

https://en.wikipedia.org/wiki/Happy_number

"""
class HappyNumber:
    def isHappy(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        return n == 1
