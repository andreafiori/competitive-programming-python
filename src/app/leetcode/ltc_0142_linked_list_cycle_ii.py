from common.list_node import ListNode

"""
Linked List Cycle II | https://leetcode.com/problems/linked-list-cycle-ii/

https://discuss.leetcode.com/topic/2975/o-n-solution-by-using-two-pointers-without-change-anything
"""
class LinkedListCycleII:

    def detect_cycle(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Two points
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

