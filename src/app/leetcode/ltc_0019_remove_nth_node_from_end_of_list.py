"""
Leetcode Problem 19: Remove Nth Node From End of List | https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from app.leetcode.ltc_0021_merge_two_sorted_lists import ListNode

class RemoveNthNodeFromEndOfList:

    def solution(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        curr = slow.next
        slow.next = curr.next
        return head
