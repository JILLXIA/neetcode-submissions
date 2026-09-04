class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort then do backtrace
        candidates.sort()

        result = []
        path = []

        def backtrace(sum: int, index:int):
            if sum == target:
                result.append(list(path))
                return

            if sum > target:
                return
            if index >= len(candidates):
                return 

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                sum += candidates[i]
                backtrace(sum, i + 1)
                sum -= candidates[i]
                path.pop()
        backtrace(0, 0)
        return result