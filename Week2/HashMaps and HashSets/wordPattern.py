class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        sentence = str.split(' ')
        if len(pattern) != len(sentence):
            return False
        if len(set(pattern)) != len(set(sentence)):
            return False
        myDict = dict()
        for i in range(len(sentence)):
            if pattern[i] in myDict and myDict[pattern[i]] != sentence[i]:
                return False
            elif pattern[i] not in myDict:
                myDict[pattern[i]] = sentence[i]
        return True
                
        