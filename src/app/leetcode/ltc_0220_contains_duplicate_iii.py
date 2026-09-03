"""
Contains Duplicate III | Leetcode 220 | Hard | https://leetcode.com/problems/contains-duplicate-iii/

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

class ContainsDuplicateIII:

    def solution(self, nums: list[int], index_diff: int, value_diff: int) -> bool:
        """
        :type nums: List[int]
        :type index_diff: int
        :type value_diff: int
        :rtype: bool
        """
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucket_num, offset = (v / value_diff, 1) if value_diff else (v, 0)
            for idx in range(bucket_num - offset, bucket_num + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= value_diff:
                    return True

            buckets[bucket_num] = nums[i]
            if len(buckets) > index_diff:
                # Remove the bucket which is too far away. Beware of zero value_diff.
                del buckets[nums[i - index_diff] / value_diff if value_diff else nums[i - index_diff]]

        return False
