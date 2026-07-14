class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        start_node = []

        for num in nums_set:
            if (num - 1) in nums_set:
                continue
            else:
                start_node.append(num)
        
        result = 1
        tmp_len = 1

        for start in start_node:
            while start + tmp_len in nums_set:
                tmp_len += 1
            result = max(result, tmp_len)
            tmp_len = 1
        return result
