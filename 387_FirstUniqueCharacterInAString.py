class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        mp = {}
        mp2 = {}
        
        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]] += 1
            else:
                mp[s[i]] = 1
                if mp[s[i]] not in mp2:
                    mp2[s[i]] = i
        #print(mp)
        #print(mp2)
        
        for key,index in mp.items():
            if index == 1:
                return mp2[key]
                
        
        
        return -1
        