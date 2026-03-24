from common.tree_node import TreeNode

"""
Second Minimum Node In A Binary Tree | https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
"""
class SecondMinimumNodeInABinaryTree:

    def find_second_minimum_value(self, root: TreeNode) -> int:
        if not root:
            return -1
        ans = float('inf')
        min_val = root.val
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if min_val < curr.val < ans:
                ans = curr.val
            elif curr.val == min_val:
                stack.append(curr.left)
                stack.append(curr.right)
        return ans if ans < float('inf') else -1
