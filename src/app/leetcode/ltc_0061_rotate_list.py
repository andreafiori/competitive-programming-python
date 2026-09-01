"""
Leetcode Problem: 61. Rotate List | https://leetcode.com/problems/rotate-list/

"""

from app.leetcode.ltc_0021_merge_two_sorted_lists import ListNode

class RotateList:

    def solution(self, head: 'ListNode', k: int) -> ListNode:
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
            return self.solution(head, k)
        else:
            while fast.next:
                fast = fast.next
                slow = slow.next
            return self._rotate(head, fast, slow)

    def _rotate(self, head: ListNode, fast: ListNode, slow: ListNode) -> ListNode:
        fast.next = head
        head = slow.next
        slow.next = None
        return head
