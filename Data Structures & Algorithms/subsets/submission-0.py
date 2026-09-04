class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrace(nums: List[int], index: int):
            nonlocal path
            result.append(list(path))
            if index >= len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrace(nums, i + 1)
                path.pop()
        backtrace(nums, 0)
        return result
            