"""

IPO | leetcode 502 | https://leetcode.com/problems/ipo/

min-heap to track capital and max-heap to track profits

"""

import heapq

class IPO:
    def find_maximized_capital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        max_heap = []
        min_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_heap)

        for _ in range(k):
            while min_heap and min_heap[0][0] <= w:
                _, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -1 * p)
            if not max_heap:
                break
            w += -1 * heapq.heappop(max_heap)

        return w
