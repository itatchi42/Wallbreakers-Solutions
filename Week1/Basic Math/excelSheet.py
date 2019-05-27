class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if not s:
            return 0
        num = 0
        x = 0
        for char in reversed(s):
            num += pow(26, x) * (letters.index(char) + 1)
            x += 1
        return num
            
            