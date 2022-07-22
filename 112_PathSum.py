# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        
        def dfs(node , currentSum):
            if node is None:
                return False
            
            #A copy of this variable is sent across the calls. Recursive Calls
            currentSum += node.val
            #print(currentSum)
            
            if node.left is None and node.right is None:
                result.append(currentSum)
            
            dfs(node.left , currentSum)
            dfs(node.right , currentSum)
            
        
        result = []
        dfs(root , 0)
        
        #print(result)
        
        if targetSum in result:
            return True
        
        return False
        
        
        
        
        