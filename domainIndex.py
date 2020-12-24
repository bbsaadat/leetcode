class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        
        largest_number = 0
        largest_number_index = 0
        
        #start for
        for i in range(len(nums)):
            #start if
            if nums[i] > largest_number:
                largest_number = nums[i]
                largest_number_index = i
            #end if
        #end for
        
        #start for
        for i in range(len(nums)):
            if i == largest_number_index:
                continue
            if nums[i]*2 > largest_number:
                return -1
        #end for
        return largest_number_index
        