"""
Leetcode Problem: 83. Remove Duplicates from Sorted List | https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""

from typing import Optional
from app.common.list_node import ListNode

class Solution:
    def solution_one(self, head):
        if head is None:
            return None
        pos = head
        while pos is not None and pos.next is not None:
            if pos.val == pos.next.val:
                pos.next = pos.next.next
            else:
                pos = pos.next
        return head

    def solution_two(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur:
            while cur.next and cur.next.val == cur .val:
                cur.next = cur.next.next
            cur = cur.next

        return head
