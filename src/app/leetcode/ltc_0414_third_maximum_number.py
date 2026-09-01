"""
Leetcode Problem: 414. Third Maximum Number | https://leetcode.com/problems/third-maximum-number/
"""

import queue as Queue

class ThirdMaximumNumber:

    def solution(self, nums: list[int]) -> int:
        """
        :param nums: list of integers
        :return: the third maximum number if it exists, otherwise the maximum number
        """
        pq = Queue.PriorityQueue(4)
        check = set()
        for n in nums:
            if n in check:
                continue
            pq.put(n)
            check.add(n)
            if len(check) > 3:
                check.remove(pq.get())
        total = len(check)
        while total < 3 and total > 1:
            total -= 1
        return pq.get()
