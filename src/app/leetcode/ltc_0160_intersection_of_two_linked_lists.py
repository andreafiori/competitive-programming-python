"""
Intersection of Two Linked Lists | LeetCode 160 | https://leetcode.com/problems/intersection-of-two-linked-lists/

"""

from app.common.list_node import ListNode

class IntersectionOfTwoLinkedLists:
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        """
        :type head_a: ListNode
        :type head_b: ListNode
        :rtype: ListNode
        """
        if not head_a or not head_b:
            return None
        a, b = head_a, head_b
        ans = None
        while a or b:
            if not a:
                a = head_b
            if not b:
                b = head_a
            if a == b and not ans:
                ans = a
            a, b = a.next, b.next
        return ans
