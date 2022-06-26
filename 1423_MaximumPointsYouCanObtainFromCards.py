class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        left = 0
        right = len(cardPoints) - k
        
        sumVal = sum(cardPoints[right:])
        
        total = sumVal
        
        while right < len(cardPoints):
            sumVal += (cardPoints[left] - cardPoints[right])
            total = max(sumVal, total)
            left += 1
            right += 1
            
        
        return total
            
            