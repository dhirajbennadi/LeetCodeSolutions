# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        mp = {}
        
        temp = head
        
        while temp:
            if temp.val not in mp:
                mp[temp.val] = 1
            else:
                mp[temp.val] += 1
            temp = temp.next
        
        result = ListNode()
        newHead = result
        
        for key,element in mp.items():
            if element > 0:
                result.next = ListNode(key)
                result = result.next
        
        return newHead.next
                
        
        
        
        
#         numSet = set()
#         temp = head
        
#         while temp is not None:
#             numSet.add(head.val)
#             temp = temp.next
        
#         result = []
#         for element in numSet:
#             result.append(element)
#         return result
        