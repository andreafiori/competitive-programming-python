"""
Valid Number | https://leetcode.com/problems/valid-number/
"""
class ValidNumber:
    def isNumber(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        try:
            float(s)
            return True
        except:
            if '.' in s or ' ' in s:
                return False
            temp = s.split('e')
            if len(temp) == 2:
                try:
                    int(temp[0])
                    int(temp[1])
                except:
                    return False
                return True
        return False
