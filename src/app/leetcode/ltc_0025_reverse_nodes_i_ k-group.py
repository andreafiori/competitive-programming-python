"""
Leetcode Problem: Reverse Nodes in k-Group | https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

from app.common.list_node import ListNode

class ReverseNodesInKGroup:

    def solution(self, head, k):
        if head is None:
            return None
        index = 0
        last = 0
        pos = head
        temp = ListNode(-1)
        temp.next = head
        head = temp
        start = head
        while pos is not None:
            if index % k == k - 1:
                last = pos.next
                start = self.reverse_list(start, last)
                pos = start
            pos = pos.next
            index += 1
        return head.next

    def reverse_list(self, head, end):
        pos = head.next
        last = end
        next_start = pos
        while pos != end:
            head.next = pos
            last_pos = pos
            pos = pos.next
            last_pos.next = last
            last = last_pos
        return next_start


