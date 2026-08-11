# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carrier = 0
        dummy = ListNode(0)
        resultPointer = dummy
        curr1 = l1
        curr2 = l2
        while curr1 or curr2 or carrier:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            sum = (v1 + v2 + carrier) % 10
            carrier = (v1 + v2 + carrier) // 10
            
            resultPointer.next = ListNode(sum)
            resultPointer = resultPointer.next

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return dummy.next