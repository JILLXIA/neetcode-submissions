class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        if len(grid) == 0 or len(grid[0]) == 0:
            return result

        def dfs(r: int , c: int):
            # find one island and flip 1 into 0
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                dfs(i, j)
                result += 1
        return result
