class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        arr = dict()
        # Init
        for c in range(len(word2) + 1): arr[0, c] = c
        for r in range(len(word1) + 1): arr[r, 0] = r
        
        # DP step (draw it on paper to see)
        for r in range(1, len(word1)+1):
            for c in range(1, len(word2)+1):
                if word1[r-1] == word2[c-1]:
                    arr[r, c] = arr[r-1, c-1] # From diagonal
                else:
                    arr[r, c] = min(arr[r, c-1], arr[r-1, c-1], arr[r-1, c]) + 1
                
        return arr[len(word1), len(word2)]
            