class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''Two Pointers'''
        
        left = 0
        right = len(height) - 1
        
        area  = 0
        temparea  = 0
        
        while left < right:
            temparea = (right - left) * min(height[left] , height[right])
            area = max(area , temparea)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -=1 
        
        return area
        
        
        
        
        '''Brute Force does not work due to TLE'''
        left = 0
        right = 1
        
        area = 0
        temparea = 0
        
        length = len(height)
        
        while left < length:
            
            while right < length:
                w = right - left
                h = min(height[left] , height[right])
            
                temparea = w * h
            
                area = max(area , temparea)
                right += 1
            
            left += 1
            right = 0
        
        return area
            