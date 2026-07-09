from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        length = 0

        # add the first node into queue
        queue.append((0, 0))
        visit.add((0,0))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while queue:
            tmp_length = len(queue)
            for i in range(tmp_length):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    # arrived the destination
                    return length
                for direction in directions:
                    next_r = r + direction[0]
                    next_c = c + direction[1]
                    if 0 <= next_r < ROWS and 0 <= next_c < COLS and (next_r, next_c) not in visit and grid[next_r][next_c] == 0:
                        queue.append((next_r, next_c))
                        visit.add((next_r, next_c))
            length += 1
        return -1