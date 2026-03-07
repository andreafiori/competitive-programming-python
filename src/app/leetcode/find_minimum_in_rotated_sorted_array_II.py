"""
Find Minimum in Rotated Sorted Array II | https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/


"""

class FindMinimumInRotatedSortedArrayII:

    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r and nums[l] >= nums[r]:
            mid = (l + r) / 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
            else:
                # nums[l] = nums[r] = nums[mid]
                l += 1
        return nums[l]
