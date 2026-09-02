"""
LeetCode Problem: 42. Trapping Rain Water | https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

class TrappingRainWater:

    def solution(self, height: list) -> int:
        """
        :type height: list
        :rtype: int
        """
        ls = len(height)
        if ls == 0:
            return 0
        res, left = 0, 0
        while left < ls and height[left] == 0:
            left += 1
        pos = left + 1
        while pos < ls:
            if height[pos] >= height[left]:
                # there is a right bar which is no less than left bar
                res += self.rain_water(height, left, pos)
                left = pos
                pos += 1
            elif pos == ls - 1:
                # left bar is higher than all right bar
                max_value, max_index = 0, pos
                for index in range(left + 1, ls):
                    if height[index] > max_value:
                        max_value = height[index]
                        max_index = index
                res += self.rain_water(height, left, max_index)
                left = max_index
                pos = left + 1
            else:
                pos += 1
        return res

    def rain_water(self, height, start, end):
        # computer rain water
        if end - start <= 1:
            return 0
        min_m = min(height[start], height[end])
        res = min_m * (end - start - 1)
        step = 0
        for index in range(start + 1, end):
            if height[index] > 0:
                step += height[index]
        return res - step
