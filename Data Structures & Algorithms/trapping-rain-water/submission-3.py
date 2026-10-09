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
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] <= height[right]:
                result += min(leftMax, rightMax) - height[left]
                left += 1
            else:
                result += min(leftMax, rightMax) - height[right]
                right -= 1
        return result







