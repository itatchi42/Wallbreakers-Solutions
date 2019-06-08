import math
class Solution:
    def isHappy(self, n: int) -> bool:
        counter = 0
        while True:
            newNum = 0
            if math.log(n, 10) % 1: #if not power of 10
                for digit in str(n):
                    newNum += pow(int(digit), 2)
                n = newNum
            else:
                return True
            counter += 1
            if counter > 5: #determined empirically
                return False
            
                
        
        #final check: if power of 10
        
        