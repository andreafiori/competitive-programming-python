

from app.common.tree_node import TreeNode

"""
Populating Next Right Pointers in Each Node | https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
class Solution:
    def connect(self, root: TreeNode) -> None:
        """
        :type root: TreeNode
        :rtype: nothing
        """
        if root is None:
            return
        nodes = [root]
        while len(nodes) != 0:
            next_step = []
            last = None
            for node in nodes:
                if last is not None:
                    last.next = node
                if node.left is not None:
                    next_step.append(node.left)
                if node.right is not None:
                    next_step.append(node.right)
                last = node
            nodes = next_step
