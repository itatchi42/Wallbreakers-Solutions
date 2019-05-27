class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        #step1: reverse each row
        #step2: foreach row, list comprehension to convert 0 to 1
        B = []
        for x in range(0, len(A)):
            #Reverse array and switch each bit of each row
            B.append([int(y==0) for y in A[x][::-1]])
        return B