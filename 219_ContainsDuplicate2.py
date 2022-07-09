class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        
        for index,element in enumerate(nums):
            current = element
            
            if (current in mp) and (index - mp[current] <= k):
                return True
            else:
                mp[current] = index
        
        return False
                