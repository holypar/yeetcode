class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = collections.Counter(s)
        tCount = collections.Counter(t)
        
        return sCount == tCount