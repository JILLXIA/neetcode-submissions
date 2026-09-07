class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        # choice -> recursive -> undo
        # open < n
        # close < open
        def backtrace(open: int, close: int):
            if open == n and close == n:
                result.append(''.join(path))
                return

            if open < n:
                path.append("(")
                backtrace(open + 1, close)
                path.pop()

            if close < open:
                path.append(")")
                backtrace(open, close + 1)
                path.pop()
        backtrace(0, 0)
        return result
