class Solution:
    def reorganizeString(self, s: str) -> str:
        # prioritize the most frequent one
        # set a hold position
        counter = Counter(s)

        max_heap = []

        for value, cnt in counter.items():
            heapq.heappush(max_heap, (-cnt, value))
        
        hold = None

        result = []

        while max_heap:
            cnt, value = heapq.heappop(max_heap)
            cnt += 1

            result.append(value)

            if hold:
                heapq.heappush(max_heap, (hold[0], hold[1]))
                hold = None

            if cnt < 0:
                hold = (cnt, value)
        if hold:
            return ""

        return ''.join(result)