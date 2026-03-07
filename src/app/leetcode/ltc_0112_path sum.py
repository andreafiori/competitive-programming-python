"""
Path Sum | https://leetcode.com/problems/path-sum/

Given the root of a tree, check if there exists a path whose sum equals target

Method: (dfs) update curSum for each node, and return true or false for each subtree

"""

from common.tree_node import TreeNode

class PathSum:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)

    def dfs(self, root: TreeNode, curSum: int, targetSum: int) -> bool:
        if root is None:
            return False
        
        curSum += root.val
        if root.left is None and root.right is None:
            return curSum == targetSum
        
        return self.dfs(root.left, curSum, targetSum) or self.dfs(root.right, curSum, targetSum)
