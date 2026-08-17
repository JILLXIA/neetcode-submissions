# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST
        # p q both exist
        ancestor = None

        if not root or not p or not q:
            return None

        def findAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> None:
            nonlocal ancestor
            if not root or not p or not q:
                return None

            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                ancestor = root
                return None
            if p.val < root.val and q.val < root.val:
                findAncestor(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                findAncestor(root.right, p, q)
        findAncestor(root, p,q)
        return ancestor
        
