class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                result = min(result, nums[l])
                break;
            mid = l + (r - l) // 2

            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result