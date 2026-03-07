"""
Balanced bst | https://leetcode.com/problems/balance-a-binary-search-tree/

Given a bst, check if it is balanced or not

Method: for each subtree, check if its left and right subtrees and balanced, and return the maxDepth + 1

"""

# Definition for a binary tree node.
from common.tree_node import TreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if root is None: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, max(left[1], right[1]) + 1]

        return dfs(root)[0]
