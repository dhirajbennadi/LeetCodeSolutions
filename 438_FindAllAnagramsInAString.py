class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        smap = {}
        pmap = {}
        
        for i in range(26):
            smap[chr(ord('a') + i)] = 0
            pmap[chr(ord('a') + i)] = 0
        
        for i in range(len(p)):
            if s[i] not in smap:
                smap[s[i]] = 1
            else:
                smap[s[i]] += 1
                
        for i in range(len(p)):
            if p[i] not in pmap:
                pmap[p[i]] = 1
            else:
                pmap[p[i]] += 1
        
        left = 0
        right = len(p)
        
        result = []
        
        while right <= len(s):
            #print(right,left ,len(s), result)
            #print(smap,pmap)
            if smap == pmap:
                result.append(left)
            
            if right != len(s):
                if s[right] not in smap:
                    smap[s[right]] = 1
                else:
                    smap[s[right]] += 1
            
            smap[s[left]] -= 1
            
            left += 1
            right += 1
    
        return result
            
            
        
        