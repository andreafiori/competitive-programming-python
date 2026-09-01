"""
Can Place Flowers | Leetcode 605 | Easy | https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

class CanPlaceFlowers:
    def solution(self, flower_bed, n):
        """
        :type flower_bed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flower_bed)):
            curr = flower_bed[i]
            if i - 1 >= 0:
                curr += flower_bed[i - 1]
            if i + 1 < len(flower_bed):
                curr += flower_bed[i + 1]
            if curr == 0:
                count += 1
                flower_bed[i] = 1
                if count >= n:
                    return True
        return False
