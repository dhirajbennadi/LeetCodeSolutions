class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        retval = 0
        
        for element in nums:
            retval ^= element
        
        return retval