"""
Leetcode Problem: 572. Subtree of Another Tree | https://leetcode.com/problems/subtree-of-another-tree/
"""

from app.common.tree_node import TreeNode

class SubtreeOfAnotherTree:

    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        :param s: TreeNode
        :param t: TreeNode
        :return: bool
        """
        s_res = self.pre_order(s, True)
        t_res = self.pre_order(t, True)
        return t_res in s_res

    def pre_order(self, root: TreeNode, is_left: bool) -> str:
        if root is None:
            if is_left:
                return "lnull"
            else:
                return "rnull"
        return "#" + str(root.val) + " " + self.pre_order(root.left, is_left=True) + " " + self.pre_order(root.right, is_left=False)
