"""
Merge k sorted linked lists | LeetCode 23 | https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

https://algo.monster/liteproblems/23

"""

from app.common.list_node import ListNode
from typing import List, Optional
from heapq import heapify, heappop, heappush

class MergeKSortedLists:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.

        Args:
            lists: List of head nodes of k sorted linked lists

        Returns:
            Head of the merged sorted linked list
        """
        # Add comparison method to ListNode for heap operations
        # This allows heap to compare ListNode objects by their values
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)

        # Initialize priority queue with all non-null head nodes
        priority_queue = [head for head in lists if head]

        # Convert list into a min-heap based on node values
        heapify(priority_queue)

        # Create dummy node to simplify list construction
        dummy_head = ListNode()
        current_node = dummy_head

        # Process nodes from heap until empty
        while priority_queue:
            # Extract node with minimum value
            min_node = heappop(priority_queue)

            # If extracted node has a next node, add it to heap
            if min_node.next:
                heappush(priority_queue, min_node.next)

            # Append the minimum node to result list
            current_node.next = min_node
            current_node = current_node.next

        # Return the head of merged list (skip dummy node)
        return dummy_head.next
