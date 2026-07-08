class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # this is a dummy node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr and i < index:
            curr = curr.next
            i += 1

        return curr.val if curr else -1
            

    def insertHead(self, val: int) -> None:
        curr = ListNode(val)
        curr_next = self.head.next
        self.head.next = curr
        curr.next = curr_next

        # if list was empty
        if not curr.next:
            self.tail = curr
        

    def insertTail(self, val: int) -> None:
        curr = ListNode(val)
        self.tail.next = curr
        self.tail = self.tail.next

        

    def remove(self, index: int) -> bool:
        i = 0
        pre = self.head
        curr = self.head.next
        while i < index and curr:
            i += 1
            pre = pre.next
            curr = curr.next

        if not curr:
            return False
        pre.next = curr.next
        if not curr.next:
            self.tail = pre
        return True
        

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
        
