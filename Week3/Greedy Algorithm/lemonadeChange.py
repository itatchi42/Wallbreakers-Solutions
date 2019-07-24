# Took 10 minutes (compared to 1 hr when I first did this problem 2 mo. ago...NICE!)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Runtime: O(n)
        
        fives, tens = 0, 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                tens += 1
                if not fives: # If I've got no $5
                    return False
                fives -= 1
            if bill == 20:
                if tens and fives: # If I've got at LEAST 1x$10  and 1x$5
                    tens -=1
                    fives -= 1
                elif not tens and fives >= 3: # If I've got at LEAST 3x$5
                    fives -= 3
                else: return False
        return True # Default
            
