"""
Minimum Depth of Binary Tree | leetcode 111 | https://leetcode.com/problems/minimum-depth-of-binary-tree/

"""

class MinimumDepthOfBinaryTree:

    def min_depth(self, root):
        if root is None:
            return 0
        queue = [root]
        depth, right_most = 1, root
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                break
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node == right_most:
                # reach the current level end
                depth += 1
                if node.right is not None:
                    right_most = node.right
                else:
                    right_most = node.left
        return depth

    def min_depth_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        ld = self.min_depth_recursive(root.left)
        rd = self.min_depth_recursive(root.right)
        if ld != 0 and rd != 0:
            # handle 0 case!
            return 1 + min(ld, rd)
        return 1 + ld + rd
