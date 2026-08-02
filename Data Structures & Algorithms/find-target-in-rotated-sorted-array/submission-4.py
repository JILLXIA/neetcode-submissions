class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            # need to check which half is sorted and find the target in the sorted array
            # left side sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
        return -1