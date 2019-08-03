class Solution:
    # Iterative approach, 299 / 304 cases passed
    # def myPow(self, x: float, n: int) -> float:
    #     res = x
    #     if not n: return 1
    #     for y in range(abs(n)-1):
    #         res *= x
    #         if not res: break # Break early for non-repetitive calc.
    #     return res if n > 0 else 1 / res
    
    
    
    # Recursive approach (Passes 243 / 304 test cases)
    # def myPow(self, x: float, n: int) -> float:
    #     if abs(n) == 1:
    #         return x
    #     return x * self.myPow(x, abs(n) - 1) if n > 0 else 1 / (x * self.myPow(x, abs(n ) - 1)) 