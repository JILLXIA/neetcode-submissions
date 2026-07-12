class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict num: frequency 
        # maximum heap (frequency, num)

        num_frequency_dict = {}

        for num in nums:
            if num not in num_frequency_dict:
                num_frequency_dict[num] = 1
            else:
                num_frequency_dict[num] += 1

        max_heap = []

        for num, frequency in num_frequency_dict.items():
            heapq.heappush(max_heap, (-frequency, num))

        result = []

        while k > 0 and max_heap:
            abs_frequency, num = heapq.heappop(max_heap)
            result.append(num)
            k -= 1
        return result