class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class PopulatingNextRightPointersInEachNodeII:

    # def connect(self, root):
    #     """
    #     :type root: TreeLinkNode
    #     :rtype: nothing
    #     """
    # level by level
    #     if root is None:
    #         return
    #     nodes = [root]
    #     while len(nodes) != 0:
    #         next_step = []
    #         last = None
    #         for node in nodes:
    #             if last is not None:
    #                 last.next = node
    #             if node.left is not None:
    #                 next_step.append(node.left)
    #             if node.right is not None:
    #                 next_step.append(node.right)
    #             last = node
    #         nodes = next_step

    def connect(self, root: TreeLinkNode) -> None:
        dummyHead = TreeLinkNode(-1)
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
