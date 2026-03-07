"""
Binary Tree Zigzag Level Order Traversal | https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

"""

class BinaryTreeZigzagLevelOrderTraversal:
    def zig_zag(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # level order
        if root is None:
            return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left:
                    record.append(node.left)
                if node.right:
                    record.append(node.right)
            if record:
                q.append(record)
        # zigzag order
        res = []
        for index, level in enumerate(q):
            temp = [x.val for x in level]
            if index % 2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
        return res
