class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #Runtime: O(n^2)
        nums.sort() #in place sort: O(nlogn)
        res = []
        for x in range(len(nums) - 1):
            if nums[x] == nums[x + 1]:
                res.append(nums[x])
                break
        for x in range(len(nums)):
            if x + 1 not in nums:
                res.append(x + 1)
                break
        return res
        