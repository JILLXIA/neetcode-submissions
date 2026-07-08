from collections import deque
class LinkedList:
    
    def __init__(self):
        self.deque = deque()
    
    def get(self, index: int) -> int:
        temp_list = list(self.deque)
        if len(temp_list) <= index :
            return -1
        return list(self.deque)[index]

    def insertHead(self, val: int) -> None:
        self.deque.appendleft(val)

    def insertTail(self, val: int) -> None:
        self.deque.append(val)

    def remove(self, index: int) -> bool:
        temp_list = list(self.deque)
        if len(temp_list) <= index :
            return False
        temp_list.pop(index)
        self.deque = deque(temp_list)
        return True


    def getValues(self) -> List[int]:
        return list(self.deque)
        
