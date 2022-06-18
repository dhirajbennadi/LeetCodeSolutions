class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        
        for element in nums:
            if element not in mp:
                mp[element] = 1
            else:
                mp[element] += 1
         
        temp = []
        result = []
        
        for key,val in mp.items():
            temp.append(val)
            
        
        temp = sorted(temp , reverse = True)
        
        for i in range(k):
            for key,val in mp.items():
                if temp[i] == val:
                    result.append(key)
                    del mp[key]
                    break
                    
        return result