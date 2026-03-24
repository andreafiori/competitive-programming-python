"""
Symmetric tree | https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself

Method: recursively compare two copies of the same tree

"""
from app.common.tree_node import TreeNode


class SymmetricTree:

    def is_symmetric(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.mirror_visit(root.left, root.right)

    def is_symmetric_two(self, root: TreeNode) -> bool:
        def check_symm(copy1: TreeNode, copy2: TreeNode) -> bool:
            if copy1 is None and copy2 is None:
                return True
            if copy1 is None or copy2 is None:
                return False

            return (copy1.val == copy2.val) and check_symm(copy1.left, copy2.right) and check_symm(copy1.right, copy2.left)

        return check_symm(root, root)

    def mirror_visit(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        try:
            if left.val == right.val:
                if self.mirror_visit(left.left, right.right) and self.mirror_visit(left.right, right.left):
                    return True
            return False
        except:
            return False
