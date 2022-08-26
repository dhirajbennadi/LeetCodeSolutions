# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        '''Brute Force'''
        if head is None:
            return None
        
        temp = head
        result = []
        while temp:
            result.append(temp.val)
            temp = temp.next
        
        def helper(left,right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(result[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1 , right)
            
            return root
        
        return helper(0 , len(result) - 1)
        