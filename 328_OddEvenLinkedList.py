# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Optimized Solution'''
        
        oddLinkedList = ListNode()
        evenLinkedList = ListNode()
        
        temp1 = oddLinkedList
        temp2 = evenLinkedList
        count = 1
        temp = head
        
        while temp:
            if count % 2 == 0:
                evenLinkedList.next = ListNode(temp.val)
                evenLinkedList = evenLinkedList.next
            else:
                oddLinkedList.next = ListNode(temp.val)
                oddLinkedList = oddLinkedList.next
            
            temp = temp.next
            count += 1
            
        evenLinkedList.next = None
        oddLinkedList.next = temp2.next
        
        dummy = temp1.next
        
        head = temp1.next

        return head        
        
        
        '''Brute Force'''
        count = 1
        evenList = []
        oddList = []
        
        temp = head
        while temp:
            if count % 2 == 0:
                evenList.append(temp.val)
            else:
                oddList.append(temp.val)
            
            temp = temp.next
            count += 1
        
        result = ListNode()
        dummy = result
        
        for element in oddList:
            dummy.next = ListNode(element)
            dummy = dummy.next
        for element in evenList:
            dummy.next = ListNode(element)
            dummy = dummy.next
        
        return result.next