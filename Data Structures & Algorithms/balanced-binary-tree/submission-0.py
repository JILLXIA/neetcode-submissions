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
            right = height(root.right)
            if abs(left - right) > 1:
                result = False
            return max(left, right) + 1
        height(root)
        return result