class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs, start from every 0 cell
        if len(grid) == 0 or len(grid[0]) == 0:
            return grid

        queue = deque()
        dists = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # start bfs
                    queue.append((i, j))
        count = 0
        while queue:
            size = len(queue)
            count += 1
            while size > 0:
                size -= 1
                tmpi, tmpj = queue.popleft()
                
                grid[tmpi][tmpj] = min(count, grid[tmpi][tmpj])

                for dist in dists:
                    updated_i = tmpi + dist[0]
                    updated_j = tmpj + dist[1]
                    if updated_i < 0 or updated_i >= len(grid) or updated_j < 0 or updated_j >= len(grid[0]) or grid[updated_i][updated_j] != 2147483647:
                        continue
                    queue.append((updated_i, updated_j))
                    grid[updated_i][updated_j] = count

            



                    