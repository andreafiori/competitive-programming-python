"""
Find Leaves of Binary Tree | https://leetcode.com/problems/find-leaves-of-binary-tree/
"""

class FindLeavesOfBinaryTree:

    def findLeaves(self, root):
        res = []
        self.findLeaves_helper(root, res)
        return res

    def findLeaves_helper(self, node, res):
        if node is None:
            return -1
        level = 1 + max(self.findLeaves_helper(node.left, res), self.findLeaves_helper(node.right, res))
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        return level
