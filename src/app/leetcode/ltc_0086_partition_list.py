from common.list_node import ListNode

"""
Partition List | https://leetcode.com/problems/partition-list/
"""
class PartitionList:
    """ @param head: The first node of linked list"""

    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        less = lesshead = None
        last = pos = head
        while pos is not None:
            if pos.val < x:
                if lesshead is None:
                    lesshead = pos
                else:
                    less.next = pos
                less = pos
                if head == pos:
                    last = head = pos.next
                else:
                    last.next = pos.next
            else:
                last = pos
            pos = pos.next
        if lesshead is not None:
            less.next = head
        else:
            lesshead = head
        return lesshead
