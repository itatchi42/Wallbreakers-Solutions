class Solution:
    def binaryGap(self, N: int) -> int:
        num = bin(N)[2:]
        longest, counter = 0, 0
        start = False
        for x in num:
            if x == '1' and not start:
                start = True
                continue #counter still 0 (as not to double count)
            if start:
                counter += 1
                if x == '1':
                    longest = max(longest, counter)
                    counter = 0 #reset
        return longest
        
        