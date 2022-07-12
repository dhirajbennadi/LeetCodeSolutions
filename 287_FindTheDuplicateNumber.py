class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()
        
        for element in nums:
            if element in mySet:
                return element
            mySet.add(element)
        
        

#Solution 2
        nums.sort()
        #Constant Extra Space
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]