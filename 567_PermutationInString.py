import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1map = {}
        s2map = {}
        for i in range(0,26):
            s1map[chr(ord('a') + i)] = 0
            s2map[chr(ord('a') + i)] = 0
        
        for i in range(len(s1)):
            s1map[chr(ord(s1[i]))] += 1
            s2map[chr(ord(s2[i]))] += 1
        
        # print(s1map)
        # print("******")
        # print(s2map)
        left = 0
        right = len(s1)
        
        #print(right)
        
        while right < len(s2):
            if s1map == s2map:
                return True
            
            
            if right != len(s2):
                s2map[chr(ord(s2[right]))] += 1
            #print(left)
            s2map[chr(ord(s2[left]))] -= 1
                
            left += 1
            right += 1
        
        return s1map == s2map
            
            