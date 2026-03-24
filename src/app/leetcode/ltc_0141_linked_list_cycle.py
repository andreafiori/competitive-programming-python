
from app.common.list_node import ListNode

"""
Linked List Cycle | https://leetcode.com/problems/linked-list-cycle/
"""
class LinkedListCycle:

    def hasCycle(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        # Add max and check if reach max
        if head is None:
            return False
        count = 0
        max = 100000
        pos = head
        while pos is not None:
            count += 1
            pos = pos.next
            if count > max:
                return True
        return False

    def hasCycle(self, head):
        # Hash or set
        dic = {}
        pos = head
        while pos is not None:
            try:
                dic[pos]
                return True
            except KeyError:
                dic[pos] = pos
            pos = pos.next
        return False

    def has_cycle(self, head):
        # Two points
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next

            return True
        except:
            return False