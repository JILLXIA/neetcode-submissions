class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        if len(nums) < 2:
            return []
        num_dict[nums[0]] = 0

        for i in range(1, len(nums)):
            if (target - nums[i]) in num_dict:
                return [num_dict[target - nums[i]], i]
            num_dict[nums[i]] = i
        return []