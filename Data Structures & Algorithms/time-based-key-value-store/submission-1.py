class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]
        l = 0
        r = len(values) - 1

        while l <= r :
            mid = l + (r - l) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if l - 1 < 0:
            return ""
        return values[l-1][0]