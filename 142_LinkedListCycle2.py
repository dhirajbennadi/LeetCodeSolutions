# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getStartingPoint(head: Optional[ListNode] , cycle_len : int) -> Optional[ListNode]:
        
            pointer1 = head
            pointer2 = head
        
            for _ in range(cycle_len):
                pointer1 = pointer1.next
        
            while pointer1 != pointer2:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
        
            return pointer2
        if head is None:
            return None
        def getCycleLen(head: Optional[ListNode]) -> int:
            target = head
            count = 0
            while True:
                head = head.next
                count += 1
                if head == target:
                    break
        
            return count
        
        slow = head
        fast = head
        cycleLen = -1
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                cycleLen = getCycleLen(slow)
                break
        
        return None if cycleLen == -1 else getStartingPoint(head,cycleLen)