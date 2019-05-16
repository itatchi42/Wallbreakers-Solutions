class Solution:
    def reverseVowels(self, s: str) -> str:
        #todo: get vowel indices
        vowels = 'aeiou'
        a = []
        for x in range(0, len(s)):
            if s[x].lower() in vowels:
                a.append(x)
        
        # swap only those indices
        myS = list(s)
        end = len(a)
        for x in range(0, end//2):
            temp = myS[a[x]]
            myS[a[x]] = myS[a[end-1-x]]
            myS[a[end-1-x]] = temp
        s = ''.join(myS)
        return s