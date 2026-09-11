class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        if len(grid) == 0 or len(grid[0]) == 0:
            return result

        def bfs(r: int, c: int):
            q = deque()

            q.append((r, c))
            grid[r][c] = '0'

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                node_r, node_c = q.popleft()
                for dir1, dir2 in directions:
                    new_r = node_r + dir1
                    new_c = node_c + dir2
                    if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]) or grid[new_r][new_c] == '0':
                        continue
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = '0'




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                bfs(i, j)
                result += 1
        return result



    # def numIslands(self, grid: List[List[str]]) -> int:
    #     result = 0

    #     if len(grid) == 0 or len(grid[0]) == 0:
    #         return result

    #     def dfs(r: int , c: int):
    #         # find one island and flip 1 into 0
    #         if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
    #             return
    #         grid[r][c] = '0'
    #         dfs(r + 1, c)
    #         dfs(r - 1, c)
    #         dfs(r, c + 1)
    #         dfs(r, c - 1)

    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == '0':
    #                 continue
    #             dfs(i, j)
    #             result += 1
    #     # DFS
    #     # Time complexity O(m * n)
    #     # Spcae complexity O(m * n)
    #     return result
