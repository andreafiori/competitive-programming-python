"""
Insert Interval | leetcode 57 | https://leetcode.com/problems/insert-interval/

"""

from typing import List
from app.common.interval import Interval

class Solution:
    def insert(self, intervals: List[Interval], new_interval: Interval) -> List[Interval]:
        """
        :type intervals: List[Interval]
        :type new_interval: Interval
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return [new_interval]
        intervals.sort(key=lambda x:x.start)
        pos = 0
        while pos < len(intervals):
            # left of pos
            if new_interval.end < intervals[pos].start:
                intervals.insert(pos, new_interval)
                return intervals
            # overlap with pos
            if self.check_overlap(intervals[pos], new_interval):
                temp = intervals.pop(pos)
                new_interval = self.merge_intervals(temp, new_interval)
            else:
                pos += 1
        if len(intervals) == 0 or pos == len(intervals):
            intervals.append(new_interval)
        return intervals

    def check_overlap(self, curr_int, new_int):
        if curr_int.start <= new_int.start:
            if curr_int.end > new_int.start:
                return True
        else:
            if curr_int.start <= new_int.end:
                return True
        return False

    def merge_intervals(self, int1, int2):
        temp_int = Interval()
        temp_int.start = min([int1.start, int2.start])
        temp_int.end = max([int1.end, int2.end])
        return temp_int
