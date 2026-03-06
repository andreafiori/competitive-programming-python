"""
374. Guess Number Higher or Lower | https://leetcode.com/problems/guess-number-higher-or-lower/

The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
"""
def guess(num):
    pass

class GuessNumberHigherOrLower:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin, end = 1, n
        while begin <= end:
            mid = (begin + end) / 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                begin = mid + 1
            else:
                end = mid - 1
