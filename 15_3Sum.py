class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            
#         nums.sort()
    
#     #print(nums)
    
#         pointer1 = 0
#         pointer2 = 0
#         pointer3 = 0
    
#         result = []
#         temp = []
    
#         for i in range(0,len(nums)):
#             pointer1 = nums[i]
#             for j in range(i, len(nums)):
#                 pointer2 = nums[j]
#                 for k in range(j,len(nums)):
#                     pointer3 = nums[k]
#                     if (pointer1 + pointer2 + pointer3) == 0 and (i != j) and (i != k) and (j != k):
#                         temp.append(pointer1)
#                         temp.append(pointer2)
#                         temp.append(pointer3)
#                         if temp not in result:
#                             result.append(temp)
#                         temp = []
#                         break
                    
#         return result
    
        result = []
        nums.sort()
    
        for i,a in enumerate(nums):
            #Once an element a is chosen, it should not be repeated
            if i > 0 and a == nums[i-1]:
                continue
        
            left = i+1
            right = len(nums) - 1
        
            while left < right:
            
                sum = a + nums[left] + nums[right]
            
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([a,nums[left] , nums[right]])
                    left += 1
                    #Left should not be same as previous else duplicate solution will exist
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result