"""
Four Sum | https://leetcode.com/problems/4sum/

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

Constraints:
    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109

"""

class FourSum:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        sort_nums = sorted(nums)
        ls = len(nums)
        res = {}
        pairs = {}
        for i in range(ls - 3):
            for j in range(i + 1, ls - 2):
                res_2 = sort_nums[i] + sort_nums[j]
                try:
                    pairs[target - res_2].append([i, j])
                except KeyError:
                    pairs[target - res_2] = [[i, j]]
        for key, temp in pairs.items():
            for pair in temp:
                j = pair[1] + 1
                k = ls - 1
                while j < k:
                    current = sort_nums[j] + sort_nums[k]
                    if current == key:
                        result = (sort_nums[pair[0]], sort_nums[pair[1]], sort_nums[j], sort_nums[k])
                        res[result] = True
                        j += 1
                    elif current < key:
                        j += 1
                    else:
                        k -= 1
        return res.keys()
