from app.common.list_node import ListNode

"""
Remove Linked List Elements | https://leetcode.com/problems/remove-linked-list-elements/
"""
class Solution:
    def removeElements(self, head: ListNode, val) -> ListNode:
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # add a extra head for removing head
        prehead = ListNode(-1)
        prehead.next = head
        last, pos = prehead, head
        while pos is not None:
            if pos.val == val:
                last.next = pos.next
            else:
                last = pos
            pos = pos.next
        return prehead.next

