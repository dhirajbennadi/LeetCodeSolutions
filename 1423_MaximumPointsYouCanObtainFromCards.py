class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        #Sliding Window Technique using two pointers
        left = 0
        right = len(cardPoints) - k
        
        #Calculate the sum for the first window size
        sumVal = sum(cardPoints[right:])
        
        #Keep a copy of the first sum to compare if this value is the maximum value
        total = sumVal
        
        #Slide the window until the right pointer is OOB
        while right < len(cardPoints):
            #Sum of elements outside the window
            sumVal += (cardPoints[left] - cardPoints[right])
            total = max(sumVal, total)
            #Move the window to the next position
            left += 1
            right += 1
            
        
        return total
            
            