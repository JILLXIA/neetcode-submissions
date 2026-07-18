class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # assume every character can be the start
        # two pointer
        l = 0

        result = 0

        # maintain a map 
        # length - maxf <= k

        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # check whether the window is valid
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        return result

