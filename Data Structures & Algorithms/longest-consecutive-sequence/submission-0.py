class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_deduplist = sorted(set(nums))

        result = 1

        tmp_len = 1

        for i in range(1, len(sorted_deduplist)):
            if sorted_deduplist[i] - sorted_deduplist[i-1] == 1:
                tmp_len += 1
            else:
                result = max(result, tmp_len)
                tmp_len = 1
        return max(result, tmp_len)