"""
Edit Distance | https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')

Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')
 
Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.

"""

class EditDistance:
    def minDistance(self, word1: str, word2: str) -> int:
        ls_1, ls_2 = len(word1), len(word2)
        dp = range(ls_1 + 1)
        for j in range(1, ls_2 + 1):
            pre = dp[0]
            dp[0] = j
            for i in range(1, ls_1 + 1):
                temp = dp[i]
                if word1[i - 1] == word2[j - 1]:
                    dp[i] = pre
                else:
                    dp[i] = min(pre + 1, dp[i] + 1, dp[i - 1] + 1)
                pre = temp
        return dp[ls_1]
