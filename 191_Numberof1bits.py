class Solution:
    def hammingWeight(self, n: int) -> int:
        value = 0
        count = 0
        
        for i in range(0,33):
            value = n & (1 << i)
            
            if value:
                count += 1
        
        return count