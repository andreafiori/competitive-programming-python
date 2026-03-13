"""
Permutation Sequence | https://leetcode.com/problems/permutation-sequence/
"""
class PermutationSequence:

    def getPermutation(self, n: int, k: int) -> str:
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # let permutations with first identical num be a block
        # target in (k - 1) / (n - 1)! block
        remain = range(1, n + 1)
        if k <= 1:
            return ''.join(str(t) for t in remain)
        total = 1
        for num in remain[:-1]:
            total *= num
        res = self.do_getPermutation(remain, total, n - 1, k - 1)
        return ''.join(str(t) for t in res)

    def do_getPermutation(self, remain: list[int], curr: int, n: int, k: int) -> list[int]:
        if n == 0 or k <= 0 or curr == 0:
            return remain
        # which block
        step = k / curr
        # remain k value
        k %= curr
        curr /= n
        res = [remain[step]] + self.do_getPermutation(remain[:step] + remain[step + 1:], curr, n - 1, k)
        return res
