class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        A = []
        for x in range(left, right + 1):
            if self.checkSelfDivide(x) == 0:
                A.append(x)
        return A
        
    def checkSelfDivide(self, num):
        if '0' in str(num):
            return 1
        arr = [num % int(char) for char in str(num)]
        return sum(arr)
            