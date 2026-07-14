class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        square_dict = {
            (0, 0): 0,
            (0, 1):1,
            (0, 2):2,
            (1, 0):3,
            (1, 1):4,
            (1, 2):5,
            (2, 0):6,
            (2, 1):7,
            (2, 2):8
        }

        # Time Complexity O(1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in row_set[i]) or (board[i][j] in col_set[j]) or (board[i][j] in square_set[square_dict.get((i // 3, j // 3))]):
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                square_set[square_dict.get((i // 3, j // 3))].add(board[i][j])
        return True
                

    

