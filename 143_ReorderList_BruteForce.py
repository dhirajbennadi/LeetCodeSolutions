# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        result = []
        
        dummy = head
        count = 0
    
        while(dummy):
            result.append(dummy.val)
            dummy = dummy.next
            count += 1
        
        #print(result)
        left = 0
        right = len(result) - 1
        
        dummy = head
        
        while left <= right:
            dummy.val = result[left]
            if left != right:
                dummy.next.val = result[right]
                dummy = dummy.next.next
            
            left += 1
            right -= 1
        
        
        
        
        
        