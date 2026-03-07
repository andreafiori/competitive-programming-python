"""
Validate binary search tree | leetcode  | https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
    

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

"""

import sys

class ValidateBinarySearchTree:
    # initialise a prev pointer
    def __init__(self):
        self.prev = None

    def isValidBST_one(self, root):
        return self.isVaild_helper(root, -sys.maxint - 1, sys.maxint)

    def isVaild_helper(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.isVaild_helper(root.left, minVal, root.val) and self.isVaild_helper(root.right, root.val, maxVal)

    # in-order traversal (L M R)
    # should return a sorted array
    def isValidBST_two(self, root) -> bool:

        # if this node is none, its a leaf
        if root is None:
            return True

        if not self.isValidBST_two(root.left):
            return False

        if self.prev is not None and self.prev.val >= root.val:
            return False

        self.prev = root

        return self.isValidBST_two(root.right)
