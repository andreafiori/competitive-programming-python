"""
Find Minimum in Rotated Sorted Array | https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


"""

class FindMinimumInRotatedSortedArray:

    def findMin(self, nums):
        # A[l] > A[r]
        l, r = 0, len(nums) - 1
        while l < r and nums[l] >= nums[r]:
            mid = (l + r) / 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
