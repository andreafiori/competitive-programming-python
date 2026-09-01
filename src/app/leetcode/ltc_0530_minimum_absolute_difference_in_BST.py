"""
Minimum absolute difference in BST | leetcode 530 | https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Method: dfs, inorder traversal

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

"""

from app.common.tree_node import TreeNode

class MinimumAbsoluteDifferenceInBST:
    def get_minimum_difference(self, root: TreeNode):
        min_diff = float('inf')
        prev_nod = None

        self.dfs(root, min_diff, prev_nod)
        return min_diff

    def dfs(self, node: TreeNode, min_diff, prev_nod):
        if node is None:
            return

        self.dfs(node.left, min_diff, prev_nod)

        if prev_nod != None:
            min_diff = min(min_diff, abs(node.val - prev_nod))
        prev_nod = node.val

        self.dfs(node.right, min_diff, prev_nod)
