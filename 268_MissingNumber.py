class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        impostor = 0
        #nums.sort()
    
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                impostor = i
        
    
        return impostor