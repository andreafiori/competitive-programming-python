from app.common.list_node import ListNode

"""
Swap Nodes in Pairs | https://leetcode.com/problems/swap-nodes-in-pairs/
"""
class SwapNodesInPairs:

    def swap(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev, p = dummyHead, head
        while p != None and p.next != None:
            q, r = p.next, p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummyHead.next
