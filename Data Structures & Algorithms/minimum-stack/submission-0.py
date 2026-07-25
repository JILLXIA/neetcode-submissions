class MinStack:
    # minStack = []

    def __init__(self):
        self.regularStack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.regularStack.append(val)
        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        

    def pop(self) -> None:
        self.regularStack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.regularStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
