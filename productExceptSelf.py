class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = len(nums)*[1]
        

        #start for
        for i in range(len(nums)):
            
            if i == 0:
                output[i] = nums[i]
                continue
                
            output[i] = output[i-1] * nums[i]  
        #end for
        
        # nums =   [1,2,3,4]
        # output = [1,12,8,6]
        
        right_product = None
        
        #start for
        for i in range(len(nums)-1, -1, -1):
            
            if i == len(nums)-1:
                output[i] = output[i-1]
                right_product = nums[i]
                continue
            if i == 0:
                output[i] = right_product
                break
                
            
            output[i] = output[i-1] * right_product
            right_product *= nums[i] 
            
        return output
            