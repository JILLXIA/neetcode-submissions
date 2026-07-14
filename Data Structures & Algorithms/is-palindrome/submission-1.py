class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left index, right index
        left = 0
        right = len(s) - 1
        # O(n)
        # check the isalpha(), check lower()
        while left < right:
            if s[left] == ' ' or not s[left].isalnum():
                left += 1
                continue
            if(s[right] == ' ' or not s[right].isalnum()):
                right -= 1
                continue
            if(s[left].lower() == s[right].lower()):
                left += 1
                right -= 1
            else:
                return False
        return True