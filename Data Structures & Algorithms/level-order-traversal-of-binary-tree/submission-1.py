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
            newLayer = []
            for _ in range(len(queue)):
                tmpNode = queue.popleft()
                newLayer.append(tmpNode.val)
                if tmpNode.left:
                    queue.append(tmpNode.left)
                if tmpNode.right:
                    queue.append(tmpNode.right)
            result.append(newLayer)

        return result