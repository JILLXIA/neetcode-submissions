from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use defaultdict to skip initialize the map
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in row_set[i]) or (board[i][j] in col_set[j]) or (board[i][j] in square_set[(i//3, j//3)]):
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                square_set[(i//3, j//3)].add(board[i][j])
        return True