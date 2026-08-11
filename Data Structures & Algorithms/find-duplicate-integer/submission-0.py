class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use set to dedup time complexity O(n), space complexity O(1)
        # [1, n]
        # sort the array, then go through, time complexity O(nlogn), space complexity O(1)

        slow = 0
        fast = 0
        # the repeat element always exist
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        pointer = 0
        while True:
            if pointer == slow:
                return pointer
            pointer = nums[pointer]
            slow = nums[slow]
        return -1
