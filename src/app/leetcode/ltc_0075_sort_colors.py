"""
Sort Colors | https://leetcode.com/problems/sort-colors/

https://leetcode.com/discuss/85658/sharing-c-solution-with-good-explanation
"""
class SortColors:

    def sort(self, nums: list[int]) -> None:
        """ Do not return anything, modify nums in-place instead. """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                # swap low mid
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                # swap mid high
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        return
