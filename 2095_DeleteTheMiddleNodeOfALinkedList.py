# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = head
        slow = head
        previousSlow = head
        
        temp = None
        
        while fast and fast.next:
            previousSlow = slow
            slow = slow.next
            fast = fast.next.next
            #print("Entered")
        
        if previousSlow.next is None:
            return None
        
        #print(slow.val)
        temp = slow.next
        previousSlow.next = temp
        
        return head