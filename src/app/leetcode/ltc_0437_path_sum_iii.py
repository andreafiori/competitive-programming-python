"""
Path Sum III | leetcode 437 | https://leetcode.com/problems/path-sum-iii/

"""

from app.common.tree_node import TreeNode

class PathSumIII:

    def path_sum(self, root: TreeNode, sum: int) -> int:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.path_sum_helper(root, sum, 0, {0: 1})
        return self.result

    def path_sum_helper(self, root: TreeNode, target: int, so_far: int, cache: dict):
        if root:
            # complement == 1, root->curr path
            complement = so_far + root.val - target
            if complement in cache:
                # S->E path, sum(root->S)-sum(root->E) = target
                self.result += cache[complement]
            cache[so_far + root.val] = cache.get(so_far + root.val, 0) + 1
            self.path_sum_helper(root.left, target, so_far + root.val, cache)
            self.path_sum_helper(root.right, target, so_far + root.val, cache)
            cache[so_far + root.val] -= 1
