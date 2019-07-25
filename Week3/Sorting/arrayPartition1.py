class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Runtime: O(nlog(n))
        nums.sort() # In place
        res = 0
        for x in range(0, len(nums), 2): # x += 2 each time
            res += nums[x]
        return res
    
        # Or alternatively:
        # return sum(nums[::2])
        