# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        leftPrev = dummy
        current = head
        #Phase 1, find the left node
        for i in range(left - 1):
            leftPrev = current
            current = current.next
        
        prev = None
        currentNode = current
        nextNode = current
        #Phase 2 Reverse the linked list between left and right
        for i in range(right-left+1):
            nextNode = currentNode.next
            
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
        
        #Phase 3 Update Pointers
        leftPrev.next.next = currentNode
        leftPrev.next = prev
        
        return dummy.next
        
        