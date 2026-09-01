"""
Leetcode Problem: 347. Top K Frequent Elements | https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""

from collections import Counter

import collections

class TopKFrequentElements:

    def solution_one(self, nums: list[int], k: int) -> list[int]:
        """
        :param nums: list[int]
        :param k: int
        :return: list[int]
        """
        counter = collections.Counter(nums)
        return [k for k,v in counter.most_common(k)]

    def solution_two(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        n = len(nums)

        # create buckets where index = frequency of element
        buckets = [[] for _ in range(n + 1)]
        for f in freq:
            buckets[freq[f]].append(f)

        # get k elements starting from the end of the bucket
        k_mf = []
        for x in buckets[::-1]:
            if k > 0:
                if x != []:
                    k_mf += x
                    k -= len(x)
            else:
                return k_mf
        return k_mf
