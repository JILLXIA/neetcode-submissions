# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # serialize the BST
        result = []
        if not root:
            return -1

        def serializeBST(root: TreeNode):
            # nonlocal result
            if not root:
                return

            serializeBST(root.left)
            result.append(root.val)
            serializeBST(root.right)
        serializeBST(root)
        return result[k-1]