class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Fail fast, check the length first
        if len(s) != len(t):
            return False
        
        table = [0] * 26

        for s1, t1 in zip(s, t):
            table[ord(s1)-ord('a')] += 1
            table[ord(t1)-ord('a')] -= 1
        for i in table:
            if i != 0:
                return False
        return True