import collections

"""
N-Repeated Element in Size 2N Array | https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""
class NRepeatedElementInSize2NArray:

    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = collections.Counter(A)
        return counter.most_common(1)[0][0]
