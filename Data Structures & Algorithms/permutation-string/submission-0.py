class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        s2_map = {}
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)

        l = 0
        for i in range(len(s2)):
            s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)
            if i - l + 1 > len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    s2_map.pop(s2[l])
                l += 1
            if i - l + 1 == len(s1) and s1_map == s2_map:
                return True
        return False

