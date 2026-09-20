class Solution:
    def numDecodings(self, s: str) -> int:
        # dp, from right to left
        if len(s) == 0:
            return 0

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                res = dp[i + 1]
                if i + 2 <= len(s) and 10 <= int(s[i:i+2]) <= 26:
                    res += dp[i + 2]
                dp[i] = res
        return dp[0]