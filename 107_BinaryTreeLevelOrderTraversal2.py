# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        tempResult = []
        finalResult = []
        
        
        def height(root):
            if not root:
                return -1
            
            temp = root
            
            while(temp):
                lheight = height(root.left)
                rheight = height(root.right)
                
                if lheight > rheight:
                    return lheight + 1
                else:
                    return rheight + 1
        
        def printlevel(root , level):
            if not root:
                return
            elif level == 0:
                tempResult.append(root.val)
            else:
                printlevel(root.left , level - 1)
                printlevel(root.right , level - 1)
        
        
        treeHeight = height(root)
        
        for i in range(treeHeight+1):
            printlevel(root , i)
            finalResult.append(tempResult)
            tempResult = []
        
            
        #print(finalResult)
        return finalResult[::-1]