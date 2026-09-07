class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def backtrace(start: int):
            if start >= len(s):
                result.append(list(path))
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrace(end + 1)
                    path.pop()
        backtrace(0)
        return result