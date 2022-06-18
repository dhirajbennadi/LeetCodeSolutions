class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next
        
        #Gives the mid point of the Linked List 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #Actual Mid Point Next Node
        head2 = slow.next
        
        slow.next = None
        #Reverse LinkedList
        prevNode = None
        currentNode = head2
        nextNode = head2
        
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        
        newHead1 = head
        newHead2 = prevNode #From the reversing of LinkedList
        
        '''
        while newHead2:
            print(newHead2.val)
            newHead2 = newHead2.next
        print("------------")
        while newHead1:
            print(newHead1.val)
            newHead1 = newHead1.next
            
        '''
        while newHead2:
            temp1 = newHead1.next
            temp2 = newHead2.next
            
            newHead1.next = newHead2
            newHead2.next = temp1
            
            newHead1 = temp1
            newHead2 = temp2