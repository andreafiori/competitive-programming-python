"""
Find Anagram Mappings | https://leetcode.com/problems/find-anagram-mappings/
"""
class FindAnagramMappings:

    def find(self, A: list[int], B: list[int]) -> list[int]:
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        val_index = {}
        ans = []
        for i, n in enumerate(B):
            val_index[n] = i
        for n in A:
            ans.append(val_index[n])
        return ans
