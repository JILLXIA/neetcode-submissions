class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # option1: flatten the list, but the time complexity should be O(m + n)
        # but we can use 1-d index to demonestrate it
        # r = index // n c = index % n
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            rows = mid // n
            cols = mid % n
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False