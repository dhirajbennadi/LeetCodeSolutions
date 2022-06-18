# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = head
        count = 0
        
        while(dummy):
            count += 1
            dummy = dummy.next
            
        #print(count)
        
        countOfNodeToBeRemoved = count - n
        
        if countOfNodeToBeRemoved < 0:
            return None
        elif countOfNodeToBeRemoved == 0:
            head = head.next
            return head
        
        dummy = head
        prev = head
        while(countOfNodeToBeRemoved):
            prev = dummy
            dummy = dummy.next
            countOfNodeToBeRemoved -= 1
        
        prev.next = dummy.next
        
        return head
        
        