# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        inorder_dict = {}
        for i, item in enumerate(inorder):
            inorder_dict[item] = i

        def build(preorder: List[int], inorder: List[int], preStart: int, preEnd: int, inStart: int, inEnd: int ) -> TreeNode:
            if preStart > preEnd or inStart > inEnd:
                return None
            rootVal = preorder[preStart]
            root = TreeNode(rootVal)

            inorderRootIndex = inorder_dict[rootVal] # it takes O(n) to find
            leftLength = inorderRootIndex - inStart
            rightLength = inEnd - inorderRootIndex

            root.left = build(preorder, inorder, preStart + 1, preStart + leftLength, inStart, inorderRootIndex - 1)
            root.right = build(preorder, inorder, preStart + leftLength + 1, preEnd, inorderRootIndex + 1, inEnd)
            return root

        return build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)