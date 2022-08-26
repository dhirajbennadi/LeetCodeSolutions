# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        '''O(1)'''
        l1 , l2 = headA, headB
        
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1
        
        
        
        
        
        
        '''Brute Force'''
        tempA = headA
        countA = 0
        tempB = headB
        countB = 0
        
        while tempA:
            tempA = tempA.next
            countA += 1
        
        while tempB:
            tempB = tempB.next
            countB += 1
        
        print(countA, countB)
        
        diff = 0
        flag = 0
        if countB > countA:
            diff = countB - countA
            flag = 1
        else:
            diff = countA - countB
        
        tempA = headA
        tempB = headB
        if flag == 1:
            while diff:
                tempB = tempB.next
                diff -= 1
        else:
            while diff:
                tempA = tempA.next
                diff -= 1
        
        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next
        
        
        return tempA
        
        