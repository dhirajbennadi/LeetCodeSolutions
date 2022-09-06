# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        totalList = []
        dummy = []
        
        temp = head
        
        while temp:
            if temp.val in nums:
                dummy.append(temp.val)
            else:
                if len(dummy) != 0:
                    totalList.append(dummy)
                dummy = []
                #dummy.clear()
            print(dummy)
            temp = temp.next
        
        if len(dummy) != 0:
            totalList.append(dummy)
        #print(totalList)
        
        return len(totalList)
        