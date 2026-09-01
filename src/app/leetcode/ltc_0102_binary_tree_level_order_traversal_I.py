"""
Binary tree level order traversal | leetcode 102 | https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Mthod: breadth first search

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

"""

from app.common.tree_node import TreeNode

class BinaryTreeLevelOrderTraversal:
    def level_order(self, root):
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
        return [[x.val for x in level] for level in q]

    def level_order(self, root):
        res = []
        temp_q = []

        # queue to track visits
        temp_q.append(root)
        l_temp_q = len(temp_q)

        # keep iterating till:
        # the track queue is empty
        while l_temp_q != 0:
            l_temp_q = len(temp_q)
            level = []
            for _ in range(l_temp_q):
                node = temp_q.pop(0)             # pop this node from queue  (visited)
                if node is not None:
                    level.append(node.val)      # add this node to the level
                    temp_q.append(node.left)     # add left child to queue   (to visit)
                    temp_q.append(node.right)    # add right child to queue  (to visit)
            if len(level) != 0:
                res.append(level)

        return res
