"""
Jewels and Stones | LeetCode 771 | https://leetcode.com/problems/jewels-and-stones/

"""

class JewelsAndStones:
    def num_jewels_in_stones(self, j: str, s: str) -> int:
        """
        :type j: str
        :type s: str
        :rtype: int
        """
        if len(j) == 0 or len(s) == 0:
            return 0
        j_set = set(j)
        ans = 0
        for c in s:
            if c in j_set:
                ans += 1
        return ans
