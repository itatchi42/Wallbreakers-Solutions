class Solution:
    def findComplement(self, num: int) -> int:
        #conv to binary
        length  = len(bin(num)) - 2
        num2 = int('1'*length, 2) #Get all '1s' rep. of same-length binary str
        return num ^ num2 #xor to invert
        