"""
Evaluate boolean binary tree | leetcode 2331 | https://leetcode.com/problems/evaluate-boolean-binary-tree/

"""

from app.common.tree_node import TreeNode

class EvaluateBooleanBinaryTree:
    def evaluateTree(self, node: TreeNode):
        if node.left is None and node.right is None:
            return node.val

        if node.val == 2:
            node.val = bool(self.evaluateTree(node.left)) or bool(self.evaluateTree(node.right))

        if node.val == 3:
            node.val = bool(self.evaluateTree(node.left)) and bool(self.evaluateTree(node.right))

        return node.val
