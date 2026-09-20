class Solution:
    def numDecodings(self, s: str) -> int:
        # s contains all digits
        memo = {} # key start, value = valid combination
        length = len(s)
       
        def dfs(start):
            if start >= length:
                return 1

            if start in memo:
                return memo[start]

            if s[start] == '0':
                return 0

            res = dfs(start + 1)
            if start + 1 < len(s) and 10 <= int(s[start:start+2]) <= 26:
                res += dfs(start + 2)
            memo[start] = res
            return res
        return dfs(0)
