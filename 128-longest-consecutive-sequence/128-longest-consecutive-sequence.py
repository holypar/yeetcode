class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSeen = set(nums)
        currSeq = 0
        lcs = 0
        
        for num in nums:
            if num-1 not in numSeen:
                currSeq = 0
                while num + currSeq in numSeen:
                    currSeq += 1
                
                lcs = max(lcs, currSeq)
        return lcs