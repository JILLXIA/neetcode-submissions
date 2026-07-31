class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # result should in 1 - max[piles]
        def calculate_time(rate):
            time = 0
            for pile in piles:
                if pile % rate == 0:
                    time += pile // rate
                else:
                    time += pile // rate + 1
            return time

        l = 1
        r = 1
        for pile in piles:
            if pile > r:
                r = pile
        while l <= r:
            mid = l + (r - l) // 2
            if calculate_time(mid) == h:
                r = mid - 1
            elif calculate_time(mid) > h:
                l = mid + 1
            else:
                r = mid - 1
        return l