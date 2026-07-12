class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict num: frequency 
        # maximum heap (frequency, num)

        num_frequency_dict = {}

        for num in nums:
            num_frequency_dict[num] = num_frequency_dict.get(num, 0) + 1
        # O(n)

        # set up a minimum heap but the heap size is k
        min_heap = []
        for key, value in num_frequency_dict.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = []

        while min_heap:
            feq, num = heapq.heappop(min_heap)
            result.append(num)
        return result