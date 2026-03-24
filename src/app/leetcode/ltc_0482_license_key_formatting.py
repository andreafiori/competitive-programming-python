"""
License Key Formatting | https://leetcode.com/problems/license-key-formatting/

https://leetcode.com/problems/license-key-formatting/discuss/96497/Python-solution
"""
class LicenseKeyFormatting(object):

    def license_key_formatting(self, S: str, K: int) -> str:
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        ls = len(S)
        if ls % K == 0:
            pos = K
        else:
            pos = ls % K
        res = S[:pos]
        while pos < ls:
            res += '-' + S[pos:pos + K]
            pos += K
        return res
