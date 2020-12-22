class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums:
            return 0
        
        
        index = 0
        
        #start for
        for i in range(len(nums)):
            #start if
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
            #end if
        #end for
        
        return index
                