from app.common.list_node import ListNode

class PlusOneLinkedList:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        place_stop, tail = dummy, dummy
        # find the tail
        while tail.next is not None:
            tail = tail.next
            if tail.val != 9:
                place_stop = tail
        if tail.val != 9:
            # done
            tail.val += 1
        else:
            # not yet
            place_stop.val += 1
            place_stop = place_stop.next
            # set all node behind this place to zero
            while place_stop is not None:
                place_stop.val = 0
                place_stop = place_stop.next
        if dummy.val == 0:
            return dummy.next
        return dummy
