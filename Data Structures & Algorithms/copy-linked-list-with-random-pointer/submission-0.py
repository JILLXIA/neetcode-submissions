"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # deep copy a regular list
        # create a map, map every node from original Node from new node
        if not head:
            return None
        copyHead = Node(head.val)
        curr = head
        copyCurr = copyHead
        nodeDict = {}
        while curr:
            nodeDict[curr] = copyCurr
            curr = curr.next
            if not curr:
                break
            copyNext = Node(curr.val)
            copyCurr.next = copyNext
            copyCurr = copyCurr.next
        
        copyCurr = copyHead
        curr = head
        while copyCurr:
            copyCurr.random = nodeDict.get(curr.random)
            curr = curr.next
            copyCurr = copyCurr.next
        return copyHead
            