"""
Find Leaves of Binary Tree | https://leetcode.com/problems/find-leaves-of-binary-tree/
"""
class FindLeavesOfBinaryTree:

    def find_leaves(self, root):
        res = []
        self.find_leaves_helper(root, res)
        return res

    def find_leaves_helper(self, node, res):
        if node is None:
            return -1
        level = 1 + max(self.find_leaves_helper(node.left, res), self.find_leaves_helper(node.right, res))
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        return level
