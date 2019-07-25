class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Runtime: O(nlog(n)), took me 30 min
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort() # Sort by 0th index
        newIntervals, i = [intervals[0]], 0
        for x in range(1, len(intervals)):
            curr, prev = intervals[x], newIntervals[i]
            if curr[0] >= prev[0] and curr[0] <= prev[1]:
                newIntervals[i] = [prev[0], max(prev[1], curr[1])]
            else: 
                newIntervals.append(curr)
                i += 1
        return newIntervals