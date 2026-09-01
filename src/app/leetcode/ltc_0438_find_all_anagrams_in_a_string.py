"""
Find All Anagrams in a String | leetcode 438 | https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""

class FindAllAnagramsInAString:
    def find_anagrams(self, s: str, p: str) -> list:
        """
        :type s: str
        :type p: str
        :rtype: list[int]
        """
        res = []
        if s is None or p is None or len(s) == 0 or len(p) == 0:
            return res
        char_map = [0] * 256
        for c in p:
            char_map[ord(c)] += 1
        left, right, count = 0, 0, len(p)
        while right < len(s):
            if char_map[ord(s[right])] >= 1:
                count -= 1
            char_map[ord(s[right])] -= 1
            right += 1
            if count == 0:
                res.append(left)
            if right - left == len(p):
                if char_map[ord(s[left])] >= 0:
                    count += 1
                char_map[ord(s[left])] += 1
                left += 1
        return res
