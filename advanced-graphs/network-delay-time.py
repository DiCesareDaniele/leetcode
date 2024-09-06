'''
https://leetcode.com/problems/network-delay-time
'''

import heapq

class Solution:
    # pylint: disable-next=invalid-name
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u - 1].append((w, v - 1))

        visited = set()
        distances = [1e10] * n
        distances[k - 1] = 0
        heap = [(0, k - 1)]
        time = 0
        while len(heap) > 0:
            dist, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            time = max(time, dist)

            for w, v in graph[u]:
                if v in visited:
                    continue
                dist_j = dist + w
                if dist_j < distances[v]:
                    distances[v] = dist_j
                    heapq.heappush(heap, (dist_j, v))
        return time if len(visited) == n else -1
