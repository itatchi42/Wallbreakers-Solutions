class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        #maximize # candies sister can get, ensuring that brother gets same #
        #if set <= len(candies)//2, then return len(set)
        #else if set > len(candies)//2, return len(candies)//2
        #Runtime: O(1)
        if not candies:
            return 0
        length = len(set(candies))
        if length <= len(candies) // 2:
            return length
        else:
            return len(candies) // 2
        
        #more concise, optimized solution
        # if not candies:
        #     return 0
        # return min(len(set(candies)), len(candies)//2)
        