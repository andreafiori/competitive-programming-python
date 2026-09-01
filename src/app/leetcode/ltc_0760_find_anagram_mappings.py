"""
Find Anagram Mappings | leetcode 760 | https://leetcode.com/problems/find-anagram-mappings/
"""

class FindAnagramMappings:

    def anagram_mappings(self, a: list, b: list) -> list:
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        val_index = {}
        ans = []
        for i, n in enumerate(b):
            val_index[n] = i
        for n in a:
            ans.append(val_index[n])
        return ans
