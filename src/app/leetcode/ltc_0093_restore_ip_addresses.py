"""
Leetcode 93. Restore IP Addresses | https://leetcode.com/problems/restore-ip-addresses/
"""

class RestoreIpAddresses:

    def solution(self, s: str) -> list[str]:
        """
        :param s: str
        :return: list[str]
        """
        ls = len(s)
        if ls == 0 or ls > 12:
            return []
        res = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    m = ls - i - j - k
                    if m > 0 and m <= 3:
                        add1 = s[0:i]
                        add2 = s[i:i + j]
                        add3 = s[i + j:i + j + k]
                        add4 = s[i + j + k:]
                        if self.is_valid(add1) and self.is_valid(add2) and \
                                        self.is_valid(add3) and self.is_valid(add4):
                            res.append(add1 + '.' + add2 + '.' + add3 + '.' + add4)
        return res

    def is_valid(self, add: str) -> bool:
        """
        :param add: str
        :return: bool
        """
        if len(add) == 1:
            return True
        if add[0] == '0':
            return False
        if int(add) <= 255:
            return True
        return False
