class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        time_stack = []
        for p, s in sorted(pair)[::-1]:
            if len(time_stack) == 0:
                time_stack.append((target - p) / s)
            elif (target - p) / s <= time_stack[-1]:
                continue
            else:
                time_stack.append((target - p) / s)
        return len(time_stack)