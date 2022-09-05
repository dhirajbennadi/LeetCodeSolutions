# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        toBeSorted = []
        while head:
            toBeSorted.append(head.val)
            head = head.next
            
        toBeSorted.sort()
        #print(toBeSorted)
        
        head = ListNode(0)
        dummy = head
        
        
        for element in toBeSorted:
            dummy.next = ListNode(element)
            dummy = dummy.next
        
        return head.next