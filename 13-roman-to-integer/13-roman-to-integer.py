class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and lookup[s[i]] < lookup[s[i+1]]:
                total = total + lookup[s[i+1]] - lookup[s[i]]
                i += 2
            else:
                total += lookup[s[i]]
                i += 1
        return total