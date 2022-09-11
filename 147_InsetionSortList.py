# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        toSort = []
        
        while temp:
            toSort.append(temp.val)
            temp = temp.next
        
        #print(toSort)
        
        #Use Insertion Sort to sort the number
        toSort.sort()
        
        dummy = ListNode()
        
        temp2 = dummy
        
        for i in range(len(toSort)):
            temp2.next = ListNode(toSort[i])
            temp2 = temp2.next
        
        
        return dummy.next