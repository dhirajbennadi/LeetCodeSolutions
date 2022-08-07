class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''Brute Force'''
        
        nums1 = []
        nums2 = []
        nums3 = []
        
        for element in nums:
            if element > pivot:
                nums2.append(element)
            elif element < pivot:
                nums1.append(element)
            else:
                nums3.append(element)
        
        for i in range(len(nums1)):
            nums[i] = nums1[i]
        for j in range(len(nums3)):
            nums[len(nums1) + j] = nums3[j]
        
        for k in range(len(nums2)):
            nums[len(nums1) + len(nums3) + k] = nums2[k]
        
        return nums