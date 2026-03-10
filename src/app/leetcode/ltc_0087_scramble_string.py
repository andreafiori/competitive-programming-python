"""
. Scramble String | https://leetcode.com/problems/scramble-string/
"""
class ScrambleString:

    def isScramble(self, s1: str, s2: str, memo={}):
        # recursive with memo
        # Check with sorted is fundamental, otherwise TLE
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) <= len(s2) <= 1:
            return s1 == s2
        if s1 == s2:
            return True
        if (s1, s2) in memo:
            return memo[s1, s2]
        n = len(s1)
        for i in range(1, n):
            a = self.isScramble(s1[:i], s2[:i], memo) and self.isScramble(s1[i:], s2[i:], memo)
            if not a:
                b = self.isScramble(s1[:i], s2[-i:], memo) and self.isScramble(s1[i:], s2[:-i], memo)
            if a or b:
                memo[s1, s2] = True
                return True
        memo[s1, s2] = False
        return False

    # def isScramble(self, s1, s2):
    #     # dp TLE
    #     if s1 == s2:
    #         return True
    #     if len(s1) != len(s2):
    #         return False
    #     ls = len(s1)
    #     letters = [0] * 26
    #     for i in range(ls):
    #         letters[ord(s1[i]) - ord('a')] += 1
    #         letters[ord(s2[i]) - ord('a')] -= 1
    #     for i in range(26):
    #         if letters[i] != 0:
    #             return False
    #     dp = [[[False] * ls for i in range(ls)] for i in range(ls + 1)]
    #     for i in range(ls):
    #         for j in range(ls):
    #             dp[1][i][j] = (s1[i] == s2[j])
    #
    #     for cur_len in range(2, ls + 1):
    #         for i in range(ls - cur_len + 1):
    #             for j in range(ls - cur_len + 1):
    #                 dp[cur_len][i][j] = False
    #                 for k in range(1, cur_len):
    #                     if dp[cur_len][i][j]:
    #                         break
    #                     dp[cur_len][i][j] = dp[cur_len][i][j] or (dp[k][i][j] and dp[cur_len - k][i + k][j + k])
    #                     dp[cur_len][i][j] = dp[cur_len][i][j] or (dp[k][i + cur_len - k][j] and dp[cur_len - k][i][j + k])
    #     return dp[ls][0][0]


