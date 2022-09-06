# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        head2 = slow
        
        prevPtr = None
        currentPtr = head2
        nextPtr = head2
        
        while currentPtr:
            nextPtr = nextPtr.next
            
            currentPtr.next = prevPtr
            prevPtr = currentPtr
            currentPtr = nextPtr
        
        temp1 = head
        temp2 = prevPtr
        
        while temp2:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
            
        
        return True
            
            
        
        