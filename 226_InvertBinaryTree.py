# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        #First Invert the left and right nodes of the root
        temp = root.left
        root.left = root.right
        root.right = temp
        
        #Recursively call the invertTree function on the left and right of each subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        
        return root