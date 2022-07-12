class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        #Sort the elements of the special floors 
        special.sort()
        #Use the two pointer strategy 
        start = bottom
        end = top
        maxlen = 0
        #The maxlen is the difference between the current floor and special floor
        for element in special:
            diff = element - start
            
            maxlen = max(maxlen,diff)
            #Update the floor to the next number of the special floor
            start = element + 1
        
        #Corner case to include the last element and top floor
        maxlen = max(maxlen, end - special[len(special) - 1])
        
        return maxlen
#         left = 0
#         right = 0
#         maxlen = 0
        
#         for i in range(bottom , top + 1, 1):
#             print(i , left,right,maxlen)
#             if i not in special:
#                 right += 1
#             else:
#                 left = right
            
#             maxlen = max(maxlen, right - left)
            
        
#         return maxlen
            
            