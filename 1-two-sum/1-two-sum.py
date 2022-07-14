class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCount = {} 
        
        for i, num in enumerate(nums):
            if target-num in numCount:
                return [numCount[target-num], i]
            numCount[num] = i
        
        return False 
