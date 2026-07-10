class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        indegree = [0] * n


        for s, d in edges:
            adj[s].append(d)
            indegree[d] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            tmp = queue.popleft()

            result.append(tmp)
            for next_node in adj[tmp]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        if len(result) < n:
            return []
        return result

