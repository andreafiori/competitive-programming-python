"""
Combination Sum II | Leetcode 40 | Medium | https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

"""

class CombinationSumII:
    def solution(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        :type candidates: list[int]
        :type target: int
        :rtype: list[list[int]]
        """
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    # check if this number is used
                    if len(temp) > 0 and temp[-1] >= j:
                        continue
                    # store index
                    temp.append(j)
                    dp[i].append(temp)
        res = []
        check = {}
        for temp in dp[target]:
            value = [candidates[t] for t in temp]
            try:
                check[str(value)] += 1
            except KeyError:
                check[str(value)] = 1
                res.append(value)
        return res
