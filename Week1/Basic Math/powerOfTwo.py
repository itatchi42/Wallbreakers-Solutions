import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # return math.log2(n) % 1 == 0 #return true if is sq root
    
        #Alternate solution (check for one bit in binary):
        # if n <= 0:
        #     return False
        # val = str(bin(n))
        # return val.count('1') == 1