"""
Find Peak Element | https://leetcode.com/problems/find-peak-element/

https://leetcode.com/discuss/88467/tricky-problem-tricky-solution

"""

class FindPeakElement:
    def find(self, nums):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] < nums[mid+1]:
                start= mid + 1
            else:
                end = mid
        return start
