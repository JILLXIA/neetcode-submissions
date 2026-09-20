class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums) # maximum amount we can robe for index i
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[len(nums) - 1]
