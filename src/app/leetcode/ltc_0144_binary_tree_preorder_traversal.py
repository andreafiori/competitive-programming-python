"""
Binary Tree Preorder Traversal
"""

from ..leetcode.tree_node import TreeNode

class BinaryTreePreorderTraversal:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res

