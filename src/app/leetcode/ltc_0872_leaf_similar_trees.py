"""
Leaf-similar trees | leetcode 872 | https://leetcode.com/problems/leaf-similar-trees/

Match the leaves of both trees

"""

from common.tree_node import TreeNode

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def getLeaves(root):
            if root is None:
                return

            getLeaves(root.left)
            if root.left is None and root.right is None:
                self.leaves.append(root.val)
            getLeaves(root.right)

        self.leaves = []
        getLeaves(root1)
        leaves1 = self.leaves

        self.leaves = []
        getLeaves(root2)
        leaves2 = self.leaves

        return leaves1 == leaves2