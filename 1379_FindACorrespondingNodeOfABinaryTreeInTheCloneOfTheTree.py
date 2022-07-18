# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if original is not None:
            if original == target:  
                return cloned
        
            dummy = self.getTargetCopy(original.left, cloned.left , target)
            if dummy is not None:
                return dummy
            else:
                dummy2 = self.getTargetCopy(original.right, cloned.right , target)
                if dummy2 is not None:
                    return dummy2
                else:
                    return None
        
        return None