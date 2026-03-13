from common.list_node import ListNode

"""
Rotate List | https://leetcode.com/problems/rotate-list/
"""
class RotateList:

    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        while k and fast.next:
            fast = fast.next
            length += 1
            k -= 1

        if k != 0:
            k = (k + length - 1) % length # original k % length
            return self.rotate_right(head, k)
        else:
            while fast.next:
                fast = fast.next
                slow = slow.next
            return self.rotate(head, fast, slow)

    def rotate(self, head: ListNode, fast: ListNode, slow: ListNode) -> ListNode:
        fast.next = head
        head = slow.next
        slow.next = None
        return head
