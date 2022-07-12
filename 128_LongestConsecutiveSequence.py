class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        left = 0
        right = 0
        maxLen = 1
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                right += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                left = right
            
            maxLen = max(maxLen , right - left + 1)
        
        return maxLen
    
#Solution 2 O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longestSequence = 0
        
        for num in nums:
            currentNum = num
            currentStreak = 1
            
            while currentNum + 1 in nums:
                currentNum += 1
                currentStreak += 1
            
            longestSequence = max(longestSequence, currentStreak)

