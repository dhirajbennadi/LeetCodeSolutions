# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        mp = {}
        
        dummy = head
        
        while dummy:
            if dummy.val not in mp:
                mp[dummy.val] = 1
            else:
                mp[dummy.val] += 1
        
            dummy = dummy.next
        
        result = ListNode()
        newHead = result
        
        for key,element in mp.items():
            if mp[key] == 1:
                result.next = ListNode(key)
                result = result.next
        
        return newHead.next
        
        
        