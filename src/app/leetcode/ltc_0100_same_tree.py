"""
Same tree | leetcode 100 | https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

"""

from app.common.tree_node import TreeNode

class SameTree:

    def solution(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q:
            return True
        try:
            left = right = True
            if p.val == q.val:
                left = self.solution(p.left, q.left)
                right = self.solution(p.right, q.right)
                return (left and right)
        except:
            return False
        return False

    def solution(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        l_result = self.solution(p.left, q.left)
        n_result = p.val == q.val
        r_result = self.solution(p.right, q.right)

        return l_result and n_result and r_result