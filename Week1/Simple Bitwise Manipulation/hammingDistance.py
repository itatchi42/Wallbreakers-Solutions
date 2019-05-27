class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if len(bin(x)) == len(bin(y)):
            longest = bin(x)
            shortest = bin(y)
        else:
            longest = max(bin(x), bin(y), key = len)
            shortest = min(bin(x), bin(y), key = len)
            
        shortest = '0b' + '0'*(len(longest) - len(shortest)) + str(shortest)[2:] #pad
        print(longest)
        print(shortest)
        return bin(int(longest, 2) ^ int(shortest, 2)).count('1')  #num. places they differ
        
        #concise soln:
        # return bin(x ^ y).count('1')