from app.leetcode.ltc_0021_merge_two_sorted_lists import MergeTwoSortedLists, ListNode

import pytest

class TestMergeTwoLists:
    @staticmethod
    def list_to_linked_list(values: list[int]) -> ListNode | None:
        dummy = ListNode()
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

    @staticmethod
    def linked_list_to_list(head: ListNode | None) -> list[int]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        return values

    @pytest.fixture
    def merge_two_sorted_lists(self) -> MergeTwoSortedLists:
        return MergeTwoSortedLists()

    @pytest.mark.parametrize(
        "list1, list2, expected",
        [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([], [0], [0]),
            ([1], [], [1]),
            ([1], [2], [1, 2]),
            ([2], [1], [1, 2]),
            ([-10, -5, 0], [-6, -3, 2], [-10, -6, -5, -3, 0, 2]),
            ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),
        ],
    )
    def test_merge_two_lists(
        self,
        merge_two_sorted_lists: MergeTwoSortedLists,
        list1: list[int],
        list2: list[int],
        expected: list[int],
    ) -> None:
        head1 = self.list_to_linked_list(list1)
        head2 = self.list_to_linked_list(list2)

        result = merge_two_sorted_lists.solution(head1, head2)

        assert self.linked_list_to_list(result) == expected

    def test_both_lists_empty(self, merge_two_sorted_lists: MergeTwoSortedLists) -> None:
        result = merge_two_sorted_lists.solution(None, None)

        assert result is None

    def test_first_list_empty(self, merge_two_sorted_lists: MergeTwoSortedLists) -> None:
        head2 = self.list_to_linked_list([1, 2, 3])

        result = merge_two_sorted_lists.solution(None, head2)

        assert self.linked_list_to_list(result) == [1, 2, 3]

    def test_second_list_empty(self, merge_two_sorted_lists: MergeTwoSortedLists) -> None:
        head1 = self.list_to_linked_list([1, 2, 3])

        result = merge_two_sorted_lists.solution(head1, None)

        assert self.linked_list_to_list(result) == [1, 2, 3]

    def test_reuses_original_nodes(self, merge_two_sorted_lists: MergeTwoSortedLists) -> None:
        head1 = self.list_to_linked_list([1, 3])
        head2 = self.list_to_linked_list([2, 4])

        original_nodes = {
            id(head1),
            id(head1.next),
            id(head2),
            id(head2.next),
        }

        result = merge_two_sorted_lists.solution(head1, head2)

        # No new data nodes should have been created.
        current = result
        while current:
            assert id(current) in original_nodes
            current = current.next