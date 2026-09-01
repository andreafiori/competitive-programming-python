"""
Maximum Product of Three Numbers | leetcode 628 | https://leetcode.com/problems/maximum-product-of-three-numbers/
"""

from functools import reduce

class MaximumProductOfThreeNumbers:

    def solution_reduce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # Check min1*min2*max1 and max1*max2*max3
        return max(reduce(lambda x, y: x * y, nums[:2]) * nums[-1],
                   reduce(lambda x, y: x * y, nums[-3:]))

    def solution_two(self, nums):
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)
