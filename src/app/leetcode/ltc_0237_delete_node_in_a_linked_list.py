"""
Delete Node in a Linked List | leetcode 237 | https://leetcode.com/problems/delete-node-in-a-linked-list/

"""

from app.leetcode.insertion_sort_list import ListNode

class DeleteNodeInALinkedList:
    def solution(self, node: 'ListNode') -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next