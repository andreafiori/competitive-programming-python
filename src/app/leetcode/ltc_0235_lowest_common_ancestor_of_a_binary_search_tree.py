from common.tree_node import TreeNode

"""
Lowest Common Ancestor of a Binary Search Tree | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
class LowestCommonAncestorOfABinarySearchTree:

    def find(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use the BST to reduce the search space
        if p is None or q is None or root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.find(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.find(root.right, p, q)
        else:
            return root
