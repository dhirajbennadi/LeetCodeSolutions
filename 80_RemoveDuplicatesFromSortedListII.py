class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        mp = {}
        
        for element in nums:
            if element in mp:
                mp[element] += 1
            else:
                mp[element] = 1
        
        count = 0
        for key,value in mp.items():
            if value >= 2:
                for i in range(2):
                    nums[count + i] = key
                count += 2
            else:
                nums[count] = key
                count += 1
        
        return count