import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # convert edges to adj metric
        graph = {}

        for i in range(n):
            graph[i] = []

        for s, d, w in edges:
            graph[s].append([d,w])

        # initialize a heap
        min_heap = []
        heapq.heappush(min_heap, [0, src]) # push [weight, node]
        shortest = {}

        while min_heap:
            weight, node = heapq.heappop(min_heap)

            if node in shortest:
                continue
            else:
                shortest[node] = weight
                for d, w in graph[node]:
                    if d not in shortest:
                        heapq.heappush(min_heap, [weight + w, d])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest

