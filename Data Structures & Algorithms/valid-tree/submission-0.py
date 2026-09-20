class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check whether the graph has circle
        # We can treat it as DAG? No!!
        # 1. Exactly n - 1 edges 2. all nodes are connected
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        queue = deque()
        visited = set()
        visited.add(0)

        queue.append(0)
        
        while queue:
            curr_node = queue.popleft()

            for next_node in adj[curr_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
        return len(visited) == n
        