class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # no duplicate -> hashset
        # two pointer
        if len(s) == 0:
            return 0
        non_dup_substring = set()
        l = 0
        r = 1
        
        non_dup_substring.add(s[l])
        result = len(non_dup_substring)
        while r < len(s):
            while s[r] in non_dup_substring and l < r:
                non_dup_substring.remove(s[l])
                l += 1
            non_dup_substring.add(s[r])
            result = max(result, len(non_dup_substring))
            r = r + 1
        return result
        # Time complexity O(n)