"""
Leetcode Problem: 24. Swap Nodes in Pairs | https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from app.common.list_node import ListNode

class Solution:

    def solution(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev, p = dummy_head, head
        while p != None and p.next != None:
            q, r = p.next, p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy_head.next
