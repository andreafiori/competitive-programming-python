"""
First Missing Positive | https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
    Input: nums = [1,2,0]
    Output: 3
    Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2
    Explanation: 1 is in the array but 2 is missing.

Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1
    Explanation: The smallest positive integer 1 is missing.
 

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1

"""

class FirstMissingPositive:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.com/discuss/86025/java-clean-o-n-solution-with-explanation
        ls = len(nums)
        index = 0
        while index < ls:
            # nums[nums[index] - 1] == nums[index] means that the num is in right position
            if nums[index] <= 0 or nums[index] > ls or nums[nums[index] - 1] == nums[index]:
                index += 1
            else:
                # swap current num to correct position
                pos = nums[index] - 1
                nums[index], nums[pos] = nums[pos], nums[index]
        res = 0
        while res < ls and nums[res] == res + 1:
            res += 1
        return res + 1
