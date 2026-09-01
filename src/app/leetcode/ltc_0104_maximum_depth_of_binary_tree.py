"""
Max depth of binary tree | leetcode 104 | https://leetcode.com/problems/maximum-depth-of-binary-tree/

given the root of a binary tree, return its maximum depth.

method: recursively increment left and right count for each new node and return max

Definition for a binary tree node.

"""

class MaximumDepthOfBinaryTree:

    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        ld = self.max_depth(root.left)
        rd = self.max_depth(root.right)
        return 1 + max(ld, rd)

    def max_depth_recursive(self, root):
        return self.find_depth(root) + 1

    def find_depth(self, node):
        if node is None:
            return -1

        ldepth = self.find_depth(node.left)
        rdepth = self.find_depth(node.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1
