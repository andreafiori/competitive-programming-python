"""
Leetcode Problem: 129. Sum Root to Leaf Numbers | https://leetcode.com/problems/sum-root-to-leaf-numbers/

"""

from app.leetcode.ltc_0094_binary_tree_inorder_traversal import TreeNode


class SumRootToLeafNumbers:

    def solution(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        # bfs with queue
        queue = [(root, root.val)]
        while len(queue) > 0:
            curr, curr_value = queue.pop(0)
            if curr.left is None and curr.right is None:
                res += curr_value
                continue
            if curr.left:
                queue.append((curr.left, curr_value * 10 + curr.left.val))
            if curr.right:
                queue.append((curr.right, curr_value * 10 + curr.right.val))
        return res
