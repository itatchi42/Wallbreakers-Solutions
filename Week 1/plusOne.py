class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #todo: conv to string
        a = ''
        for x in digits:
            a += str(x)
        #todo: add 1
        num = int(a) + 1
        
        #conv back to list
        b = [int(x) for x in str(num)]
        return b
        
    