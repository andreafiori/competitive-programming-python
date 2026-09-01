"""
K Closest Points to Origin | LeetCode 973 | https://leetcode.com/problems/k-closest-points-to-origin/

"""

import heapq

class KClosestPointsToOrigin:

    def k_closest(self, points, k: int) -> list[list[int]]:
        # K smallest heaq
        return heapq.nsmallest(k, points, key=lambda x: x[0] ** 2 + x[1] ** 2)
