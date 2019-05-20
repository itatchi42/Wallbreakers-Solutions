class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return False
        
        capitals = len([x for x in word if x.isupper()])
        if word[0].isupper():
            if capitals  != len(word) and capitals != 1:
                return False
        elif capitals != 0:
            return False
        return True
            
            