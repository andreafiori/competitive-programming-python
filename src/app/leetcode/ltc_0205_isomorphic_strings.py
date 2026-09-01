"""
Isomorphic Strings | Medium | https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

    Explanation: The strings s and t can be made identical by:
        Mapping 'e' to 'a'.
        Mapping 'g' to 'd'.

Example 2:
    Input: s = "f11", t = "b23"
    Output: false
    Explanation: The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
    Input: s = "paper", t = "title"
    Output: true

"""

class IsomorphicStrings:

    def solution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = len(s)
        map_s_to_t = [0] * 127
        map_t_to_s = [0] * 127
        for i in range(ls):
            s_num, t_num = ord(s[i]), ord(t[i])
            if map_s_to_t[s_num] == 0 and map_t_to_s[t_num] == 0:
                map_s_to_t[s_num] = t_num
                map_t_to_s[t_num] = s_num
            elif map_t_to_s[t_num] != s_num or map_s_to_t[s_num] != t_num:
                return False
        return True
