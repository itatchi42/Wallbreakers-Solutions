class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        lo, hi = 0, len(nums)  
        if len(nums) == 1 and nums[0] == target:
            return 0
        while mid < hi and mid > lo:
            if nums[mid] > target:
                hi = mid
                mid = (lo + mid) // 2 # Go down
            if nums[mid] < target:
                lo = mid
                mid = (mid + hi) // 2 # Go up
            if nums[mid] == target:
                return mid
        return -1 
            