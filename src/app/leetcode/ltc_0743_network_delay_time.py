"""
Network Delay Time | leetcode 743 | https://leetcode.com/problems/network-delay-time/

"""

import collections

class Solution:

    def network_delay_time(self, times, n, k):
        # Dijkstra
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, n + 1)}
        seen = [False] * (n + 1)
        dist[k] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, n + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1
