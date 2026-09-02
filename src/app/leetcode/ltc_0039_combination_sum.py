"""
Combination Sum | Leetcode 39 | Medium | https://leetcode.com/problems/combination-sum/

"""

class CombinationSum:

    def solution(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

        :param candidates: List[int] - A list of distinct integers.
        :param target: int - The target integer.
        :return: List[List[int]] - A list of all unique combinations that sum to target.
        """
        result = []
        candidates.sort()

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i)
                combination.pop()

        backtrack(target, [], 0)
        return result
