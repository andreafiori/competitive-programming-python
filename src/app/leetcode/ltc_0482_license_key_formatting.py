"""
License Key Formatting | Leetcode 482 | Medium | https://leetcode.com/problems/license-key-formatting/

https://leetcode.com/problems/license-key-formatting/discuss/96497/Python-solution
"""

class LicenseKeyFormatting:
    def solution(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = s.upper().replace('-', '')
        ls = len(s)
        if ls % k == 0:
            pos = k
        else:
            pos = ls % k
        res = s[:pos]
        while pos < ls:
            res += '-' + s[pos:pos + k]
            pos += k
        return res
