class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (distance, [x, y])

        point_heap = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(point_heap, (-distance, point))

            if len(point_heap) > k:
                heapq.heappop(point_heap)
        result = []

        while point_heap:
            result.append(heapq.heappop(point_heap)[1])
        return result

