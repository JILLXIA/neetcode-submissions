class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # find way to dedup
        nums.sort()

        result = []
        path = []

        def backtrace(index: int):
            result.append(list(path))

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrace(i + 1)
                path.pop()
        backtrace(0)

        return result