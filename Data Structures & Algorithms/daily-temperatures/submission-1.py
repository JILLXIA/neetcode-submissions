class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        stack = []

        for i in range(length - 1, -1, -1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if len(stack) == 0:
                result[i] = 0
            else:
                result[i] = stack[-1] - i
            stack.append(i)
        return result