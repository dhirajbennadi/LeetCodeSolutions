# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        '''Brute Force'''
        if head is None:
            return None
        
        dummy1 = ListNode(0,None)
        dummy2 = ListNode(0,None)
        
        
        
        ptr = head
        ptr1 = dummy1
        ptr2 = dummy2
        
        while ptr:
            #print(ptr.val)
            if ptr.val >= x:
                ptr2.next = ListNode(ptr.val)
                #print(ptr2.val)
                ptr2 = ptr2.next
            else:
                ptr1.next = ListNode(ptr.val)
                #print(ptr1.val)
                ptr1 = ptr1.next
            ptr = ptr.next
        
        
        #dummy1.next = ptr1
    
        current = dummy1.next
        
        prev = None
        
        while current:
            prev = current
            current = current.next
        
        if dummy2.next is not None:
            if prev is None:
                return dummy2.next
            prev.next = dummy2.next
        
        return dummy1.next
                