from app.leetcode.ltc_0023_merge_k_sorted_lists import MergeKSortedLists
from app.common.list_node import ListNode

class TestMergeKSortedLists:

    def test_merge_k_lists(self):
        list1 = ListNode(1, ListNode(4, ListNode(5)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        list3 = ListNode(2, ListNode(6))

        lists = [list1, list2, list3]

        merger = MergeKSortedLists()
        merged_head = merger.merge_k_lists(lists)

        # Convert the merged linked list to a Python list for easy comparison
        result = []
        while merged_head:
            result.append(merged_head.val)
            merged_head = merged_head.next

        assert result == [1, 1, 2, 3, 4, 4, 5, 6], f"Expected [1, 1, 2, 3, 4, 4, 5, 6], but got {result}"
