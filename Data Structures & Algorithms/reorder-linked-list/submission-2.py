# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow fast pointer, and then merge
        # find half way point, reverse the second half, then merge
        # 2 4 6 8, slow: 4 fast: 6, slow: 6, fast: null
        # 2 4 6 8 10, slow: 4 fast: 6, slow:6, fast:10, slow: 6 fast: null
        if not head or not head.next:
            return
        preSlow = ListNode(0)
        
        slow = head
        preSlow.next = slow
        fast = head
        while fast and fast.next:
            preSlow = slow
            slow = slow.next
            fast = fast.next.next
        
        preSlow.next = None

        pre = None
        while slow:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        
        # merge head and pre
        curr1 = head
        curr2 = pre
        idx = 0
        dummy = ListNode(0)
        dummy.next = head
        while curr1 and curr2:
            if idx % 2 == 0:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
            dummy = dummy.next
            idx += 1
        dummy.next = curr1 or curr2
            
        
        

