"""
First Unique Character in a String | leetcode 387 | https://leetcode.com/problems/first-unique-character-in-a-string/

"""

class FirstUniqueCharacterInAString:

    def first_uniq_char(self, s: str) -> int:
        """
        :param s: str
        :return: int
        """
        count_map = {}
        for c in s:
            count_map[c] = count_map.get(c, 0) + 1
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1
