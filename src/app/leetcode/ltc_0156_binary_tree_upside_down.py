"""
Binary Tree Upside Down | https://leetcode.com/problems/binary-tree-upside-down/


"""

from common.tree_node import TreeNode

class BinaryTreeNode(TreeNode):

    def upside_down_binary_tree(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node, parent, parent_right = root, None, None
        while node is not None:
            left = node.left
            node.left = parent_right
            parent_right = node.right
            node.right = parent
            parent = node
            node = left
        return parent