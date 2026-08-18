# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # current node compare with the maximum of the parents
        count = 0

        # edge case, tree is none
        if not root:
            return 0

        def findGoodNodes(root: TreeNode, maxValue: int) -> None:
            nonlocal count

            if not root:
                return
            if root.val >= maxValue:
                count += 1
            findGoodNodes(root.left, max(maxValue, root.val))
            findGoodNodes(root.right, max(maxValue, root.val))
        findGoodNodes(root, root.val - 1)
        return count
