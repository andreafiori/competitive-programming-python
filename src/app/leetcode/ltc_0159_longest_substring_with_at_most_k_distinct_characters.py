"""
Longest Substring with At Most K Distinct Characters | https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""
class LongestSubstringWithAtMostKDistinctCharacters:
    def find_longest(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = [0] * 256
        i, numDistinct, maxLen = 0, 0, 0
        for j in range(len(s)):
            # udpate j
            if count[ord(s[j])] == 0:
                numDistinct += 1
            count[ord(s[j])] += 1
            # udpate i
            while numDistinct > k:
                count[ord(s[i])] -= 1
                if count[ord(s[i])] == 0:
                    numDistinct -= 1
                i += 1
            maxLen =  max(j - i + 1, maxLen)
        return maxLen
