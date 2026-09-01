"""
N repeated element in size 2N array | leetcode 961 | https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

"""

import collections

class NRepeatedElementInSize2NArray:
    def solution(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        counter = collections.Counter(a)
        return counter.most_common(1)[0][0]
