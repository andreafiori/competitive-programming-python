"""
Longest substring without repeating characters | leetcode 3 | https://leetcode.com/problems/longest-substring-without-repeating-characters

Sliding window; remove elements until last occurence of current duplicate

"""

class LongestSubstringWithoutRepeatingCharacters:

    def solution_one(self, s):
        char_map = {}
        for i in range(256):
            char_map[i] = -1
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            # Note that when charMap[ord(s[j])] >= i, it means that there are
            # duplicate character in current i,j. So we need to update i.
            if char_map[ord(s[j])] >= i:
                i = char_map[ord(s[j])] + 1
            char_map[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len

    def solution_two(self, s: str) -> int:
        ptr_l = 0
        seen = {}
        longest = 0

        for ptr_r in range(len(s)):
            while seen.get(s[ptr_r]) is not None:
                seen.pop(s[ptr_l])
                ptr_l += 1
            seen[s[ptr_r]] = True
            longest = max(ptr_r - ptr_l + 1, longest)

        return longest
