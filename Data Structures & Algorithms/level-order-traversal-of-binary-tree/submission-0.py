# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # deque
        result = []
        queue = deque()
        if not root:
            return result

        queue.append(root)
        count = 1
        while queue:
            newCount = 0
            newLayer = []
            while count > 0:
                tmpNode = queue.popleft()
                newLayer.append(tmpNode.val)
                if tmpNode.left:
                    queue.append(tmpNode.left)
                    newCount += 1
                if tmpNode.right:
                    queue.append(tmpNode.right)
                    newCount += 1
                count -= 1
            count = newCount
            result.append(list(newLayer))

        return result