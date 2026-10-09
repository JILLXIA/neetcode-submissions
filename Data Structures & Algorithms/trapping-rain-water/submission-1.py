class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        for i in range(len(height)):
            leftMax[i] = max(height[i], leftMax[i-1]) if i > 0 else height[i]

        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1]) if i < len(height) - 1 else height[i]
        
        result = 0
        for i in range(len(height)):
            result += min(leftMax[i], rightMax[i]) - height[i]

        # time complexity: O(n)
        # space complexity: O(1)
        return result