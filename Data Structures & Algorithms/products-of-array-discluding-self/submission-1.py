class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        suffix_product = []

        # [1, 1, 2, 8, 48]
        #     [48, 48, 24, 6, 1]

        # [1, -1, 0, 0, 0, 0]
        #     [0,  0, 6, 6, 3, 1]
        prefix_product.append(1)
        suffix_product = [1] * (len(nums) + 1)

        for num in nums:
            prefix_product.append(num * prefix_product[-1])
        for i in range(len(nums) - 1, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i]

        result = []

        for i in range(1, len(prefix_product)):
            result.append(prefix_product[i-1] * suffix_product[i])
        return result
