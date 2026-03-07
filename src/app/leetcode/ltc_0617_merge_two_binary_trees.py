"""
Merge Two Binary Trees | https://leetcode.com/problems/merge-two-binary-trees/

"""

from common.tree_node import TreeNode

class MergeTwoBinaryTrees:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
