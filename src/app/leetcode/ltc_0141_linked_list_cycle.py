"""
Linked List Cycle | LeetCode 141 | https://leetcode.com/problems/linked-list-cycle/

"""
class LinkedListCycle:

    def solution(self, head):
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