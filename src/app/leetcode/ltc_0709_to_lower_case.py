"""
To Lower Case | https://leetcode.com/problems/to-lower-case/
"""
class TolowerCase:

    def transform(self, str: str) -> str:
        """
        :type str: str
        :rtype: str
        """
        res = []
        gap = ord('a') - ord('A')
        for c in str:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                res.append(chr(ord(c) + gap))
            else:
                res.append(c)
        return ''.join(res)
