class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n), product for all the nums then use division
        product = 1
        zero_cnt = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        if zero_cnt == 1:
            result = [0] * len(nums)
            result[nums.index(0)] = product
            return result
        
        result = []
        for num in nums:
            result.append(int(product/num))
                
        return result