"""
Product of Array Except Self | https://leetcode.com/problems/product-of-array-except-self/
"""
class ProductOfArrayExceptSelf:

    def product_except_one(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        N = len(nums)

        # save prefix to result array
        product = 1
        for i in range(N):
            product = nums[i] * product
            result.append(product)

        # update result array as per postfix
        postfix = 1
        for i in range(N - 1, 0, -1):
            result[i] = result[i - 1] * postfix
            postfix = postfix * nums[i]
        result[0] = postfix

        return result

    def product_except_two(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans
