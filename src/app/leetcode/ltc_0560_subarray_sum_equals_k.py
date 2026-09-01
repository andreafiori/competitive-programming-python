"""
Leetcode Problem: 560. Subarray Sum Equals K | https://leetcode.com/problems/subarray-sum-equals-k/
"""

class SubarraySumEqualsK:

    def solution(self, nums: list[int], k: int) -> int:
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        sum_map = {}
        sum_map[0] = 1
        count = curr_sum = 0
        for num in nums:
            curr_sum += num
            # Check if sum - k in hash
            count += sum_map.get(curr_sum - k, 0)
            # add curr_sum to hash
            sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
        return count
