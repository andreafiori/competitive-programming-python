
"""
Container With Most Water | Leetcode 11 | Medium | https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

"""

class ContainerWithMostWater:
    def max_area(self, height):
        # skip some choices
        ls = len(height)
        lm = min(height[0], height[ls - 1])
        max_v = lm * (ls - 1)
        low = 0
        high = ls - 1
        while low < high:
            while height[low] < lm and low < ls:
                low += 1
            while height[high] < lm and high < ls:
                high -= 1
            if low > high:
                break
            m = min(height[low], height[high])
            if m * (high - low) > max_v:
                max_v = m * (high - low)
                lm = m
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_v
