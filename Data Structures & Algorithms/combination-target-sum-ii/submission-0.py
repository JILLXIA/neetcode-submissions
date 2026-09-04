class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort then do backtrace
        candidates.sort()

        result = []
        path = []

        def backtrace(candidates: List[int], target: int, sum: int, index:int):
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
                path.append(candidates[i])
                sum += candidates[i]
                backtrace(candidates, target, sum, i + 1)
                sum -= candidates[i]
                path.pop()
        backtrace(candidates, target, 0, 0)
        return result