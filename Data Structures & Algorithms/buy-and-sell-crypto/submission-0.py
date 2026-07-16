class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        if len(prices) == 1:
            return 0

        l = 0

        while l < len(prices):
            r = l + 1
            while r < len(prices) and prices[r] > prices[l]:
                result = max(result, prices[r] - prices[l])
                r += 1
            l = r
        return result