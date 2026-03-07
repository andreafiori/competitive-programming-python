"""
Contains Duplicate III | https://leetcode.com/problems/contains-duplicate-iii/

You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

Example 1:
    Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
    Output: true
    Explanation: We can choose (i, j) = (0, 3).
    We satisfy the three conditions:
    i != j --> 0 != 3
    abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
    abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:
    Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
    Output: false
    Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.


Constraints:
    2 <= nums.length <= 105
    -109 <= nums[i] <= 109
    1 <= indexDiff <= nums.length
    0 <= valueDiff <= 109

"""

from typing import List

class ContainsDuplicateIII:

    def check(self, nums: List[int], k: int, t: int) -> bool:
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # https://discuss.leetcode.com/topic/19991/o-n-python-using-buckets-with-explanation-10-lines
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v / t, 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] / t if t else nums[i - k]]

        return False
