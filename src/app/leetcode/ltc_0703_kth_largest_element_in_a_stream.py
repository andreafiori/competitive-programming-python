
import heapq

"""
Kth Largest Element in a Stream | http://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
class KthLargest:

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        # build min heap
        heapq.heapify(self.nums)
        # remove n - k smallest number
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        # add to heaq if it's less then k
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            # if len(heaq) == k, and val greater than smallest num
            # then pop smallest num than add val to heap
            heapq.heapreplace(self.nums, val)
        # return k largest
        return self.nums[0]
