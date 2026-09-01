"""
Leetcode 117: Populating Next Right Pointers in Each Node II | https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:

    def connect(self, root):
        dummy_head = TreeLinkNode(-1)
        pre = dummy_head
        while root is not None:
            if root.left is not None:
                pre.next = root.left
                pre = pre.next
            if root.right is not None:
                pre.next = root.right
                pre = pre.next
            root = root.next
            if root is None:
                pre = dummy_head
                root = dummy_head.next
                dummy_head.next = None
