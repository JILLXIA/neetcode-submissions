import heapq
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x:int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

        self.components -= 1
        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        min_heap = []

        uf = UnionFind(n)
        for s, d, w in edges:
            heapq.heappush(min_heap, [w, s, d])

        result = 0
        while min_heap:
            w, s, d = heapq.heappop(min_heap)
            if uf.union(s, d):
                result += w
        
        if uf.components != 1:
            return -1
        return result




