"""
Binary tree preorder traversal | leetcode 94 | https://leetcode.com/problems/binary-tree-preorder-traversal/
method: node, left subtree, right subtree recursively

"""

from common.tree_node import TreeNode

class BinaryTreePreordertraversal:
    def preorderTraversal(self, root: TreeNode):
        travList = []
        self.traverse(root, travList)
        return travList

    # Traverse right subtree and add nodes
    def traverse(self, root: TreeNode, travList: list):
        if root is None:
            return None

        # Add this node
        travList.append(root.val)
        # traverse left subtree and add nodes
        self.traverse(root.left, travList)
        self.traverse(root.right, travList)
