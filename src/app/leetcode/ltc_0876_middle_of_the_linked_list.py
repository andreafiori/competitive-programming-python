
from app.leetcode.ltc_0002_add_two_numbers import ListNode

"""
Middle of the Linked List | https://leetcode.com/problems/middle-of-the-linked-list/
"""
class MiddleOfTheLinkedList:

    def middle_node(self, head: ListNode) -> ListNode:
        # Fast point is 2 times faster than slow point
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
