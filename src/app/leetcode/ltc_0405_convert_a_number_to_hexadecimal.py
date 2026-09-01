
"""
Contains a Number to Hexadecimal | Leetcode 405 | Easy | https://leetcode.com/problems/convert-a-number-to-hexadecimal/
"""

class ConvertANumberToHexadecimal:
    def solution(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        # letter map
        mp = '0123456789abcdef'
        ans = ''
        for _ in range(8):
            # get last 4 digits
            # num & 1111b
            n = num & 15
            # hex letter for current 1111
            c = mp[n]
            ans = c + ans
            # num = num / 16
            num = num >> 4
        #strip leading zeroes
        return ans.lstrip('0')

    def solution_two(self, num):
        return self._to_hex(num, 32)[2:]

    def _to_hex(self, val, nbits):
        return hex((val + (1 << nbits)) % (1 << nbits))

    def solution_recursive(self, num, h=''):
        return (not num or h[7:]) and h or self.solution_recursive(num // 16, '0123456789abcdef'[num % 16] + h)
