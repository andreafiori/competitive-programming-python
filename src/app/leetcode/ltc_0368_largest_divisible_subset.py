"""
Largest Divisible Subset | LeetCode 368 | https://leetcode.com/problems/largest-divisible-subset/

"""

class LargestDivisibleSubset:
    def solution(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        S = {-1: set()}
        for x in sorted(nums):
            # S[x] is the largest subset with x as the largest element
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))

    def solution_two(self, nums: list[int]) -> list[int]:
        S = {-1: set()}
        for num in sorted(nums):
            candicate = []
            for key in S:
                if num % key == 0:
                    candicate.append(S[key])
            # max previous with curr
            S[num] = max(candicate, key=len) | {num}
        return list(max(S.values(), key=len))