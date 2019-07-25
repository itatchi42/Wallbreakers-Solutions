class Solution:
    # Runtime: O(log(n))
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo, hi = 0, len(A) - 1
        mid = (lo + hi) // 2
        mntn = mid
        
        while mid < hi:
            if A[mid - 1] > A[mid]: # If left bigger
                hi = mid - 1
            elif A[mid + 1] > A[mid]: # If right bigger
                lo = mid + 1
            else: break # Found mountain
            mid = (lo + hi) // 2
            mntn = mid if A[mntn] < A[mid] else mntn # Conditionally set mntn
        return mntn
            
        