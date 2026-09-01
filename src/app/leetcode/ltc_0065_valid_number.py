"""
Leetcode Problem: 65. Valid Number | https://leetcode.com/problems/valid-number/
"""

class ValidNumber:

    def solution(self, s: str) -> bool:
        s = s.strip()
        ls, pos = len(s), 0
        if ls == 0:
            return False
        if s[pos] == '+' or s[pos] == '-':
            pos += 1
        is_numeric = False
        while pos < ls and s[pos].isdigit():
            pos += 1
            is_numeric = True
        if pos < ls and s[pos] == '.':
            pos += 1
            while pos < ls and s[pos].isdigit():
                pos += 1
                is_numeric = True
        elif pos < ls and s[pos] == 'e' and is_numeric:
            is_numeric = False
            pos += 1
            if pos < ls and (s[pos] == '+' or s[pos] == '-'):
                pos += 1
            while pos < ls and s[pos].isdigit():
                pos += 1
                is_numeric = True
        # print(pos, ls, is_numeric)
        if pos == ls and is_numeric:
            return True
        return False
