class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0 , 1
        maxValue = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxValue = max(maxValue, profit)
            else:
                #Very Important
                left = right
            right += 1
                
        return maxValue