"""
First Unique Character in a String | https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0

Explanation:
    The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
    Input: s = "loveleetcode"
    Output: 2

Example 3:
    Input: s = "aabb"
    Output: -1


Constraints:
    1 <= s.length <= 105
    s consists of only lowercase English letters.

"""

class FirstUniqueCharacterInAString:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        count_map = {}
        for c in s:
            count_map[c] = count_map.get(c, 0) + 1
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1

    # def firstUniqChar(self, s):
    #     min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
