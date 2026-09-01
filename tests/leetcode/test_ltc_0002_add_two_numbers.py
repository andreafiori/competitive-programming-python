import pytest

from app.leetcode.ltc_0002_add_two_numbers import AddTwoNumbers, ListNode

@pytest.fixture
def add_two_numbers():
    """Provide a fresh AddTwoNumbers instance for each test."""
    return AddTwoNumbers()

class TestAddTwoNumbers:
    def list_to_linked_list(self, arr):
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_add_two_numbers(self, add_two_numbers):

        # Example 1: 342 + 465 = 807
        l1 = self.list_to_linked_list([2, 4, 3])
        l2 = self.list_to_linked_list([5, 6, 4])
        result = add_two_numbers.solution(l1, l2)
        assert self.linked_list_to_list(result) == [7, 0, 8]

        # Example 2: 0 + 0 = 0
        l1 = self.list_to_linked_list([0])
        l2 = self.list_to_linked_list([0])
        result = add_two_numbers.solution(l1, l2)
        assert self.linked_list_to_list(result) == [0]

        # Example 3: 9999999 + 9999 = 10009998 (reversed: 89990001)
        l1 = self.list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_linked_list([9, 9, 9, 9])
        result = add_two_numbers.solution(l1, l2)
        assert self.linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]
