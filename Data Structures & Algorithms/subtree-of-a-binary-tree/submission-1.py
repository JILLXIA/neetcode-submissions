# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # convert both tree to str and check whether subRoot str is a substr for root str
        return self.treeToStr(subRoot) in self.treeToStr(root)

    def treeToStr(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'
        leftStr = self.treeToStr(root.left)
        rightStr = self.treeToStr(root.right)
        # print(leftStr + str(root.val) + rightStr)
        return str(root.val) + leftStr + rightStr
        # Time complexity: O(m + n) + O(m * n) (substr search)
        # Space complexity: O(m + n)
        '''
        If you used something like KMP for the substring search, you could reduce it to:

Time: O(n + m), Space: O(n + m).
        '''



