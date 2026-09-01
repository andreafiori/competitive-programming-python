"""
Leetcode Problem: 404. Sum of Left Leaves | https://leetcode.com/problems/sum-of-left-leaves/
"""

from app.common.tree_node import TreeNode

class SumOfLeftLeaves:

    def solution(self, root: TreeNode) -> int:
        stack = [root]
        res = 0
        while len(stack) > 0:
            curr = stack.pop(0)
            if curr is not None:
                if curr.left is not None:
                    if curr.left.left is None and curr.left.right is None:
                        res += curr.left.val
                stack.insert(0, curr.right)
                stack.insert(0, curr.left)
        return res
