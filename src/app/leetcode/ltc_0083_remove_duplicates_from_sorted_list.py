
from typing import Optional
from common.list_node import ListNode

"""
Remove Duplicates from Sorted List | https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
class RemoveDuplicatesFromSortedList:
    def solution_one(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        pos = head
        while pos is not None and pos.next is not None:
            if pos.val == pos.next.val:
                pos.next = pos.next.next
            else:
                pos = pos.next
        return head

    def solution_two(self, head: ListNode) -> ListNode:
        cur = head

        while cur:
            while cur.next and cur.next.val == cur .val:
                cur.next = cur.next.next
            cur = cur.next

        return head
