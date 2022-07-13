# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''Reversing the LinkedList'''
        
        slow = head
        fast = head
        previousSlow = head
        count = 0
        
        while fast and fast.next:
            previousSlow = slow
            slow = slow.next
            fast = fast.next.next
            count += 1
        
        
        #print(count)
        #print(slow.val)
        if previousSlow.next is not None:
            current = previousSlow.next
            #print(current.val)
            previousSlow.next = None
        else:
            current = previousSlow
            previousSlow.next = None
        
        prev = None
        nextNode = current
        
        while current:
            nextNode = nextNode.next
            current.next = prev
            prev = current
            current = nextNode
            
            
        
        head1 = head
        head2 = prev
        maxSum = 0
        
        dummy = head2
        
        while dummy:
            print(dummy.val)
            dummy = dummy.next
        
        while head1 and head2:
            #print(head1.val , head2.val , head1.val + head2.val)
            maxSum = max(maxSum, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next
        
        return maxSum
        
        
        
        '''Brute Force'''
        temp = head
        nums = []
        
        while temp:
            nums.append (temp.val)
            temp = temp.next
    
        maxSum = 0
        for i in range(len(nums) // 2):
            currentSum = nums[i] + nums[len(nums) - 1 - i]
            
            maxSum = max(maxSum , currentSum)
        
        
        return maxSum