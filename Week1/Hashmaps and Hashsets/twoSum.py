class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {x[1] : x[0] for x in enumerate(nums)} #dict comprehension
        for i in range(0, len(nums)):
            if (target - nums[i]) in myDict:
                if myDict[target - nums[i]] != i: #not same indx
                    return [i, myDict[target - nums[i]]]
        
                
