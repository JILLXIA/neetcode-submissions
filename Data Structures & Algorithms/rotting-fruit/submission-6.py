class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # add rotten fruit into queue
        # use bfs expand to check
        # check all the cell whether we have fresh fruit

        queue = deque()
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        count = -1
        dists = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        if fresh == 0:
            return 0

        while queue:
            size = len(queue)
            while size > 0:
                tmp_i, tmp_j = queue.popleft()
                for dist in dists:
                    updated_i = tmp_i + dist[0]
                    updated_j = tmp_j + dist[1]
                    if updated_i < 0 or updated_j < 0 or updated_i >= len(grid) or updated_j >= len(grid[0]) or grid[updated_i][updated_j] != 1:
                        continue
                    grid[updated_i][updated_j] = 2
                    fresh -= 1
                    queue.append((updated_i, updated_j))
                size -= 1
            count += 1

        
        return count if fresh == 0 else -1