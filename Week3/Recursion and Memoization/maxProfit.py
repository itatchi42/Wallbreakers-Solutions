class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 2: GREEDY- Find a small one? Save it!
        smallest, diff = float('inf'), 0
        for val in prices:
            smallest = min(smallest, val)
            diff = max(diff, val - smallest)
        return diff