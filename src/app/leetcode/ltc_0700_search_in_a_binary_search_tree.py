"""
Leetcode 700. Search in a Binary Search Tree | https://leetcode.com/problems/search-in-a-binary-search-tree/

"""

from app.common.tree_node import TreeNode

class Solution:
    # def searchBST(self, root, val):
    #     """
    #     :type root: TreeNode
    #     :type val: int
    #     :rtype: TreeNode
    #     """
    #     # Recursive
    #     if not root:
    #         return None
    #     if root.val == val:
    #         return root
    #     elif root.val > val:
    #         return self.searchBST(root.left, val)
    #     else:
    #         return self.searchBST(root.right, val)

    def searchBST(self, root, val):
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return root
