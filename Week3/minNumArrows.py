# Never thought of sorting by the 2nd coord...needed to refer to other solns here.
# Runtime: O(logn)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: 
            return 0
        points = sorted(points, key = lambda x: x[1]) # Sort by 2nd coord
        numArrows, end = 0, float('-inf')
        for pt in points:
            if pt[0] > end:
                numArrows += 1
                end = pt[1]
        return numArrows
            