class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(n) = max(f(i-1), f(i-2) + nums[i])
        if not nums: return 0
        if len(nums) <= 3: return max(nums)
        ans1, ans2 = 0, 0
        i1, i2 = 0, 0
        for x in nums[:-1]: # Avoid last ele
            temp = i1
            i1 = i2
            i2 = max(temp + x, i1)
        ans1 = i2
        
        i1, i2 = 0, 0
        for x in nums[1:]: # Avoid first ele
            temp = i1
            i1 = i2
            i2 = max(temp + x, i1)
        return max(i2, ans1)