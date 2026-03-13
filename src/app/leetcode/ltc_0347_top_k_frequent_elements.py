import collections

from collections import Counter

"""
Top K Frequent Elements | https://leetcode.com/problems/top-k-frequent-elements/
"""
class TopKFrequentElements:

    def top_k_frequent1(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        N = len(nums)

        # create buckets where index = frequency of element
        buckets = [[] for x in range(N + 1)]
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

    def top_k_frequent2(self, nums: list[int], k: int) -> list[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        return [k for k,v in counter.most_common(k)]
