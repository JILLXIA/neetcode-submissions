class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums) # O(n)

        return len(num_set) != len(nums)