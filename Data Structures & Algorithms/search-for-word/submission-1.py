class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(n * m * k)
        result = False

        if len(word) == 0 or len(board) == 0 or len(board[0]) == 0:
            return result

        def backtrace(r: int, c: int, count: int):
            nonlocal result
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or count > len(word) or board[r][c] != word[count]:
                return
            if count == len(word) - 1:
                result = True
                return
            # mask visited
            temp = board[r][c]
            board[r][c] = '#'
            count += 1
            backtrace(r + 1, c, count)
            backtrace(r - 1, c, count)
            backtrace(r, c + 1, count)
            backtrace(r, c - 1, count)
            count -= 1
            board[r][c] = temp


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    backtrace(i, j, 0)
                if result:
                    return result
        return result
                    
        