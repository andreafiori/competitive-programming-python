"""
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [3,2,1]

Example 2:
    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    Output: [4,6,7,5,2,9,8,3,1]

Example 3:
    Input: root = []
    Output: []

Example 4:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""

class BinaryTreePostorderTraversal:
    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     # Recursion
    #     if root is None:
    #         return []
    #     res = []
    #     self.postorderHelp(root, res)
    #     return res
    #
    # def postorderHelp(self, node, stack):
    #     if node is None:
    #         return
    #     self.postorderHelp(node.left, stack)
    #     self.postorderHelp(node.right, stack)
    #     stack.append(node.val)

    # def postorderTraversal(self, root):
    #     # Stack
    #     if root is None:
    #         return []
    #     res = []
    #     stack = [root]
    #     while len(stack) > 0:
    #         curr = stack.pop()
    #         res.insert(0, curr.val)
    #         if curr.left is not None:
    #             stack.append(curr.left)
    #         if curr.right is not None:
    #             stack.append(curr.right)
    #     return res

    def postorderTraversal(self, root):
        if root is None:
            return []
        res = []; stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                res.append(curr)
                continue
            stack.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res
