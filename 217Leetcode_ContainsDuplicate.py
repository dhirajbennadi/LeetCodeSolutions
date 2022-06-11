class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictNums = {}
        retVal = False
        
        for element in nums:
            if element not in dictNums:
                dictNums[element] = 1
            else:
                dictNums[element] += 1
                return True
        
        return retVal
#         for key,value in dictNums.items():
#             if value > 1:
#                 retVal = True
        
#         return retVal