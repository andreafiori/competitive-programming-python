"""
Closest Binary Search Tree Value | Leetcode 270 | Easy | https://leetcode.com/problems/closest-binary-search-tree-value/

"""

from app.common.tree_node import TreeNode
class ClosestBinarySearchTreeValue:

    def solution(self, root: TreeNode, target: float) -> float:
        kid = root.left if target < root.val else root.right
        if not kid:
            return root.val
        kid_min = self.solution(kid, target)
        return min((kid_min, root.val), key=lambda x: abs(target - x))
