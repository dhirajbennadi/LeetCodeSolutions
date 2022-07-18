# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if root is None:
            return 0
        
        def inorder(root):
            if root is None:
                return 
            
            inorder(root.left)
            if root.val >= low and root.val <= high:
                result.append(root.val)
            inorder(root.right)
        
        result = []
        inorder(root)
        resultSum = 0
        
        for element in result:
            resultSum += element
        
        return resultSum