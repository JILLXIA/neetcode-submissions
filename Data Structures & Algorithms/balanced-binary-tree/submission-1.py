# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # default result value is true
        result = True

        def height(root) -> int:
            nonlocal result
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                result = False
                return -1
            return max(left, right) + 1
        height(root)
        return result