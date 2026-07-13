class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre: [1,1,2,8]
        # suf: [48, 24, 6, 1]

        # pre: [1, -1, 0, 0, 0]
        # suf: [0, 6, 6, 3, 1]

        pre = [1] * len(nums)
        suf = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i-1]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i+1]
        result = []

        for i in range(len(nums)):
            result.append(pre[i] * suf[i])
        return result