class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        
        index = 1
        
        #start for
        for i in range(len(nums)-1):
            #start if
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
            #end 
            
        #end for
        
        return index
        
        
        