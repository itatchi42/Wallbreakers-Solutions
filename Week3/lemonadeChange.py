#Took 1 hr of debugging...
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        for curr in bills:
            if curr == 5:
                fives += 1
            if curr == 10:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1                
            if curr == 20:
                if fives < 1:
                    return False
                elif fives > 0 and tens > 0:
                    fives -= 1
                    tens -= 1
                elif fives >= 3 and tens <= 0: #if tens <= 0
                    fives -= 3
                else: 
                    return False
        return True
                