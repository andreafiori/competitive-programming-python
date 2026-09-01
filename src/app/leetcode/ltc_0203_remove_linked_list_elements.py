"""
Leetcode Problem 203: Remove Linked List Elements | https://leetcode.com/problems/remove-linked-list-elements/
"""

from common.list_node import ListNode

class RemoveLinkedListElements:

    def solution(self, head: ListNode, val: int) -> ListNode:
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # add a extra head for removing head
        prehead = ListNode(-1)
        prehead.next = head
        last, pos = prehead, head
        while pos is not None:
            if pos.val == val:
                last.next = pos.next
            else:
                last = pos
            pos = pos.next
        return prehead.next

