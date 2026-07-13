class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict num: frequency 
        # maximum heap (frequency, num)

        num_frequency_dict = {}

        for num in nums:
            num_frequency_dict[num] = num_frequency_dict.get(num, 0) + 1
        # O(n)

        #Bucket Sort, use an array, the index means the frequency

        bucket_list = [[] for _ in range(len(nums) + 1)]

        for key, value in num_frequency_dict.items():
            bucket_list[value].append(key)

        result = []
        for i in range(len(bucket_list) - 1, -1, -1):
            for num in bucket_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
        # Time complexity: O(n)
