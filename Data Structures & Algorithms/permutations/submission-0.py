class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrace():
            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrace()
                path.pop()
                used[i] = False
        backtrace()
        return result