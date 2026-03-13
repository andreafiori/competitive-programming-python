from app.common.list_node import ListNode

"""
Odd Even Linked List | https://leetcode.com/problems/odd-even-linked-list/
"""
class OddEvenLinkedList:
    def find_odd_even_list(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        if head is None:
            return None
        if head.next is None:
            return head
        even_head = even = head.next
        while odd.next is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
