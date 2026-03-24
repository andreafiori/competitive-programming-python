from app.common.tree_node import TreeNode

"""
Populating Next Right Pointers in Each Node II | https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
class PopulatingNextRightPointersInEachNodeII:

    def connect(self, root: TreeNode) -> None:
        dummyHead = TreeNode(-1)
        pre = dummyHead
        while root is not None:
            if root.left is not None:
                pre.next = root.left
                pre = pre.next
            if root.right is not None:
                pre.next = root.right
                pre = pre.next
            root = root.next
            if root is None:
                pre = dummyHead
                root = dummyHead.next
                dummyHead.next = None
