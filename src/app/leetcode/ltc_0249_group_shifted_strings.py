"""
Group Shifted Strings | LeetCode 249 | https://leetcode.com/problems/group-shifted-strings/

"""

class GroupShiftedStrings:
    def solution(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            key = self.hash_code(s)
            try:
                dic[key].append(s)
            except KeyError:
                dic[key] = [s]
        return dic.values()

    def hash_code(self, str: str) -> str:
        if str is None or len(str) == 0:
            return ''
        if len(str) == 1:
            return 'a'
        step = abs(ord(str[0]) - ord('a'))
        if step == 0:
            return str
        key = 'a'
        for ch in str[1:]:
            curr = ord(ch) - step
            if ord(ch) - step < ord('a'):
                curr += 26
            key += chr(curr)
        return key
