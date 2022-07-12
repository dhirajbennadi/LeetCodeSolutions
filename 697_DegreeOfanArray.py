class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        mp_firstIndex = {}
        mp_secondIndex = {}
        mp_countIndex = {}
        flag = False
        
        for index,element in enumerate(nums):
            if element not in mp_firstIndex:
                mp_firstIndex[element] = index
                flag = True
                
            if flag == True:
                mp_secondIndex[element] = index
            
            if element not in mp_countIndex:
                mp_countIndex[element] = 1
            else:
                mp_countIndex[element] += 1
            
            
        degree = 0
        
        for key,element in mp_countIndex.items():
            if element > degree:
                degree = element
        
        #print(degree)
        
        maxLen = len(nums)
        
        for key,element in mp_countIndex.items():
            if degree == element:
                maxLen = min(maxLen , mp_secondIndex[key] - mp_firstIndex[key] + 1)
        
        return maxLen