"""
Binary Tree Preorder Traversal | Leetcode 144 | https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

class BinaryTreePreorderTraversal:

    def solution(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.result = []
        self.preorder_traversal_helper(root)
        return self.result

    def preorder_traversal_helper(self, node):
        if node is None:
            return
        self.result.append(node.val)
        self.preorder_traversal_helper(node.left)
        self.preorder_traversal_helper(node.right)

    def preorder_traversal(self, root):
        # stack
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

