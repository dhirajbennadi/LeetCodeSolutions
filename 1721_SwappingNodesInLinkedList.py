# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head
        count = 0
        firstVal = 0
        secondVal = 0
        length = 0
        
        while temp:
            count += 1
            if count == k:
                firstVal = temp.val
            
            length += 1
            temp = temp.next
            
        temp = head
        count = 0
        while temp:
            count += 1
            if count == length + 1 - k:
                secondVal = temp.val
            
            temp = temp.next
        
        temp = head
        count = 0
        
        while temp:
            count += 1
            if count == k:
                temp.val = secondVal
            if count == length + 1 - k:
                temp.val = firstVal
            temp = temp.next
        
        return head