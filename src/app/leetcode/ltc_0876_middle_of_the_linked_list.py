"""
Middle of the Linked List | leetcode 876 | Easy | https://leetcode.com/problems/middle-of-the-linked-list/

"""

class MiddleOfTheLinkedList:
    def solution_one(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[len(res) // 2]

    def solution_two(self, head):
        # Fast point is 2 times faster than slow point
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
