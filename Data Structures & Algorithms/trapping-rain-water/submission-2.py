class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer
        if len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1

        leftMax = height[0]
        rightMax = height[len(height) - 1]

        result = 0

        while left <= right:
            if height[left] <= height[right]:
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
                
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                right -= 1
        return result







