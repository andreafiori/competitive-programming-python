"""
Partition List | leetcode 86 | https://leetcode.com/problems/partition-list/

"""

class PartitionList:

    def partition(self, head, x):
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
