class Solution:
    def longestPalindrome(self, s: str) -> str:
        # time complexity: O(n^2)
        # space complexity: O(1)

        def findPalindrome(start: int, end: int) -> str:
            while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1:end]

        maxLength = 0
        result = ''

        if len(s) <= 1:
            return s
        
        for i in range(len(s)):
            p1 = findPalindrome(i, i)
            p2 = findPalindrome(i, i + 1)

            maxLength = max(maxLength, len(p1), len(p2))

            if maxLength == len(p1):
                result = p1
            elif maxLength == len(p2):
                result = p2
        return result