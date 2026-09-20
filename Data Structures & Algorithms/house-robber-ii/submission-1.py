class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        def rob_house(start, end): 
            memo = {}
            def dfs(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])

                return memo[i]
            return dfs(start)
        return max(rob_house(0, len(nums) - 2), rob_house(1, len(nums) - 1))


            