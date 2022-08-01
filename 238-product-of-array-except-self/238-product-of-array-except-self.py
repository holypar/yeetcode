class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            prefix = product
            product *= nums[i]
            res[i] = prefix
        
        product = 1
        
        for i in range(len(nums)-1, -1,-1):
            prefix = product
            product *= nums[i]
            res[i] *= prefix
        
        return res