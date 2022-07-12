class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            #If the sum of the elements goes negative that means no values are adding to the max Subarray
            #Discard the values and start afresh
            if curSum < 0:
                curSum = 0
            
            curSum += n
            #print(curSum, maxSub)
            
            maxSub = max(maxSub, curSum)
        
        return maxSub