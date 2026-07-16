class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        l = 0
        r = len(heights) - 1

        result = 0

        while l < r:
            result = max(result, (r - l) * min(heights[l], heights[r]))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result
