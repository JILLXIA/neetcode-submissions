class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [ -cnt for cnt in count.values()] # int
        q = deque() # [number, interval]

        time = 0
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            # pop out from heap and add to queue
            if maxHeap:
                tmp = heapq.heappop(maxHeap)
                if tmp + 1 != 0:
                    q.append([tmp + 1, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
