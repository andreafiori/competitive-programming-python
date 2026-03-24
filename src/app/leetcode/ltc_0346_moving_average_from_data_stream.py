"""
Moving Average from Data Stream | https://leetcode.com/problems/moving-average-from-data-stream/
"""
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.curr_range = []

    def next(self, val: int) -> float:
        """
        :type val: int
        :rtype: float
        """
        if len(self.curr_range) == self.size:
            self.curr_range.pop(0)
        self.curr_range.append(val)
        return sum(self.curr_range) * 1.0 / len(self.curr_range)
