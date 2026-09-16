"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {}
        queue = deque()

        queue.append(node)
        while queue:
            tmp = queue.popleft()
            cloneNode = Node(tmp.val, [])
            node_map[tmp] = cloneNode
            for neighbor in tmp.neighbors:
                if neighbor not in node_map.keys():
                    queue.append(neighbor)

        for originalNode, cloneNode in node_map.items():
            for node_neighbor in originalNode.neighbors:
                cloneNode.neighbors.append(node_map[node_neighbor])
        return node_map[node]
