"""
Group anagrams | https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""

from collections import defaultdict

class GroupAnagrams:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs.sort()
        hash = {}
        for s in strs:
            key = self.hash_key(s)
            try:
                hash[key].append(s)
            except KeyError:
                hash[key] = [s]
        return hash.values()

    def hash_key(self, s: str) -> str:
        # hash string with 26 length array
        table = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            table[index] += 1
        return str(table)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped = defaultdict(list)

        for each_word in strs:
            count_of_ch = [0] * 26
            for each_ch in each_word:
                count_of_ch[ord(each_ch) - ord("a")] += 1
            grouped[tuple(count_of_ch)].append(each_word)

        return grouped.values()
