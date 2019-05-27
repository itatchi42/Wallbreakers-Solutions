class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        #todo: simply swap indices of each row    
        B = []
        for x in range(0, len(A[0])):
            B.append([y[x] for y in A])
        return B           
        