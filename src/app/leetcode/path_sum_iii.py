"""
Path Sum III | https://leetcode.com/problems/path-sum-iii/

https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
"""

from common.tree_node import TreeNode

class PathSumIII:

    def pathSumHelper(self, root, target, so_far, cache):
        if root:
            # complement == 1, root->curr path
            complement = so_far + root.val - target
            if complement in cache:
                # S->E path, sum(root->S)-sum(root->E) = target
                self.result += cache[complement]
            cache[so_far + root.val] = cache.get(so_far + root.val, 0) + 1
            self.pathSumHelper(root.left, target, so_far + root.val, cache)
            self.pathSumHelper(root.right, target, so_far + root.val, cache)
            cache[so_far + root.val] -= 1
        return

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.pathSumHelper(root, sum, 0, {0: 1})
        return self.result
