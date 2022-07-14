class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSeen = set(nums)
        currCons = 0
        longestCons = 0
        
        for num in nums:
            if num-1 not in numSeen: #signifiies the START of a sequence. 
                currCons = 0
                while num + currCons in numSeen: #check if that sequence continues
                    currCons += 1
                
                longestCons = max(currCons, longestCons)
        
        return longestCons