class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrace(nums: List[int], target: int, index: int, sum: int):
            if sum == target :
                result.append(list(path))
                return
            if sum > target:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                sum = sum + nums[i]
                backtrace(nums, target, i, sum)
                sum = sum - nums[i]
                path.pop()
        backtrace(nums, target, 0, 0)
        return result