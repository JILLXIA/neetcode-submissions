import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        min_heap = []

        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, w in edges:
            adj[s].append((d, w))
            adj[d].append((s, w))
        
        heapq.heappush(min_heap, (0,0))

        result = 0

        visit = set()

        while min_heap:
            w, d = heapq.heappop(min_heap)
            

            if d in visit:
                continue
            visit.add(d)
            result += w

            for next_node, next_weight in adj[d]:
                if next_node not in visit:
                    heapq.heappush(min_heap, (next_weight, next_node))
        if len(visit) != n:
            return -1
        return result
