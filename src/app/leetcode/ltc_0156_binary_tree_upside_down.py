"""
Binary Tree Upside Down | leetcode 156 | https://leetcode.com/problems/binary-tree-upside-down/

Given a binary tree where all the right nodes are either leaf nodes with a sibling or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes.

"""

class BinaryTreeUpsideDown:

    def upside_down_binary_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # top-down
        node, parent, parent_right = root, None, None
        while node is not None:
            left = node.left
            node.left = parent_right
            parent_right = node.right
            node.right = parent
            parent = node
            node = left
        return parent