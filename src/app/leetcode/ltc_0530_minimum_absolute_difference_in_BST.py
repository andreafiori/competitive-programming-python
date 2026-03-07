"""
Minimum absolute difference in BST | leetcode 530 | https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Method: dfs, inorder traversal

"""

from common.tree_node import TreeNode

class Solution:
    def getMinimumDifference(self, root: TreeNode):
        minDiff = float('inf')
        prevNod = None

        self.dfs(root, minDiff, prevNod)
        return minDiff

    def dfs(self, node: TreeNode, minDiff, prevNod):
        if node is None:
            return

        self.dfs(node.left)

        if prevNod != None:
            minDiff = min(minDiff, abs(node.val - prevNod))
        prevNod = node.val

        self.dfs(node.right)

