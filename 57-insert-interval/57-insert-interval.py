class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[-1]
        left = []
        right= []
        for interval in intervals:
            #start of newInterval is after current Interval; currInterval is LEFT
            if start > interval[1]:
                left.append(interval)
            elif end < interval[0]:
                right.append(interval)
            else: #overlap case
                start = min(start,interval[0])
                end = max(end,interval[1])

        return left + [[start,end]] + right
            
            