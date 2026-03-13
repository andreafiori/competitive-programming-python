from common.list_node import ListNode

"""
Merge k sorted linked lists | https://leetcode.com/problems/merge-k-sorted-lists/
"""
class MergeKSortedLists(object):

    def merge_k_lists(self, lists):
        # recursive
        if lists is None:
            return None
        elif len(lists) == 0:
            return None
        return self.merge_k(lists, 0, len(lists) - 1)

    def merge_k(self, lists, low, high):
        if low == high:
            return lists[low]
        elif low + 1 == high:
            return self.merge_two_lists(lists[low], lists[high])
        mid = (low + high) / 2
        return self.merge_two_lists(self.mergeK(lists, low, mid), self.mergeK(lists, mid + 1, high))

    def merge_two_lists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = curr = ListNode(-1)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2
        return head.next
