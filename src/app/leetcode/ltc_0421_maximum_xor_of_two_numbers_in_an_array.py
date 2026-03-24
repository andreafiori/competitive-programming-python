"""
Maximum XOR of Two Numbers in an Array | https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

https://discuss.leetcode.com/topic/63299/python-6-lines-bit-by-bit
"""
class MaxXorOfTwoNumbersInAnArray:

    def find_maximum_XOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            # use a set to remove duplicate
            prefixes = {num >> i for num in nums}
            # if there is x y in prefixes, where x ^ y = answer ^ 1
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer
