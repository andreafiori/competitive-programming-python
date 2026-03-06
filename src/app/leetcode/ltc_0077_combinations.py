"""
77. Combinations | https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    Explanation: There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
    Input: n = 1, k = 1
    Output: [[1]]
    Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
    1 <= n <= 20
    1 <= k <= n

"""

class Combinations:
    # def combine(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     candidates = range(1, n + 1)
    #     self.get_combine(res, candidates, [], k, 0)
    #     return res

    # def get_combine(self, res, candidates, prefix, k, start):
    #     # recursive
    #     if k == 0:
    #         res.append(prefix)
    #     for index in range(start, len(candidates)):
    #         self.get_combine(res, candidates,
    #                          prefix + [candidates[index]],
    #                          k - 1, index + 1)

    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 1)
        return res

    def get_combine(self, res, prefix, n, k, start):
        # recursive with only one array
        if k == 0:
            res.append(list(prefix))
        elif start <= n:
            prefix.append(start)
            self.get_combine(res, prefix, n, k - 1, start + 1)
            prefix.pop()
            self.get_combine(res, prefix, n, k, start + 1)
