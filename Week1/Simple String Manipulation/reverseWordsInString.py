class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: #short-circuit to save time
            return ''
        words = s.split(' ') #split by spaces
        for x in range(0, len(words)):
            words[x] = words[x][::-1] #reverse and save, in place
        return ' '.join(words)