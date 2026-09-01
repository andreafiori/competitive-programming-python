"""
Max depth of n-ary tree | leetcode 559 | https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Method: (dfs) return 1 + max(depths) at each node, return 1 if leaf

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

Constraints:

The total number of nodes is in the range [0, 104].
The depth of the n-ary tree is less than or equal to 1000.

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class MaxDepthOfNaryTree:
    def solution(self, root):
        if root is None:
            return 0

        depths = [self.solution(child) for child in root.children]

        if depths:
            return 1 + max(depths)

        return 1
