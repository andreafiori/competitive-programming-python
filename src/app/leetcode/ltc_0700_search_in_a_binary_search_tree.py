"""
Search in a Binary Search Tree | https://leetcode.com/problems/search-in-a-binary-search-tree/

"""

from common.tree_node import TreeNode

class SearchInABinarySearchTree:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return root
