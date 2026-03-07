"""
Count nodes equal to average of subtree | leetcode 2265 | https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

Method: dfs, update size and sum of subtree at each node and check for average

"""

from common.tree_node import TreeNode

class CountNodesEqualToAverageOfSubtree:
    def averageOfSubtree(self, root: list[TreeNode]) -> int:
        self.counter = 0
        def dfs(node):
            if node is None:
                return 0, 0

            lSize, lSum = dfs(node.left)
            rSize, rSum = dfs(node.right)

            nSize, nSum = lSize + rSize + 1, lSum + rSum + node.val
            if (nSum // nSize) == node.val:
                self.counter += 1

            return nSize, nSum

        dfs(root)
        return self.counter

