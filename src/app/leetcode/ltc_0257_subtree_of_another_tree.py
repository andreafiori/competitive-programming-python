"""
Subtree of Another Tree | https://leetcode.com/problems/subtree-of-another-tree/

https://leetcode.com/problems/subtree-of-another-tree/solution/
"""

from common.tree_node import TreeNode

class Solution:
    # 
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_res = self._preorder(s, True)
        t_res = self._preorder(t, True)
        return t_res in s_res
    
    def _preorder(self, root: TreeNode, isLeft: bool) -> str:
        if root is None:
            if isLeft:
                return "lnull"
            else:
                return "rnull"
        return "#" + str(root.val) + " " + self._preorder(root.left, True) + " " + self._preorder(root.right, False)
