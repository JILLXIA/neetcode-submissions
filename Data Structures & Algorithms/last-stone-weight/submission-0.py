class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python by default is min heap, but we need maximum heap here
        stoneHeap = [-stone for stone in stones]

        heapq.heapify(stoneHeap)

        while len(stoneHeap) > 1:
            x = heapq.heappop(stoneHeap)
            y = heapq.heappop(stoneHeap)

            if x == y:
                continue
            weight = abs(x - y)

            heapq.heappush(stoneHeap, -weight)

        return 0 if len(stoneHeap) == 0 else -heapq.heappop(stoneHeap)