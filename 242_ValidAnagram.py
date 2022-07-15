class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        smap = {}
        tmap = {}
        for i in range(len(s)):
            if chr(ord(s[i])) not in smap:
                smap[chr(ord(s[i]))] = 1
            else:
                smap[chr(ord(s[i]))] += 1
                
                
        for i in range(len(t)):
            if chr(ord(t[i])) not in tmap:
                tmap[chr(ord(t[i]))] = 1
            else:
                tmap[chr(ord(t[i]))] += 1
        
        #print(smap)
        #print(tmap)
            
        
        return smap == tmap
        