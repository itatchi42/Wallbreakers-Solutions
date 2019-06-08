class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = [x for x in 'abcdefghijklmnopqrstuvwxyz']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        myDict = dict(zip(letters, morse))
        mySet = set()
        for word in words:
            mySet.add(''.join([myDict[x] for x in word]))
        return len(mySet)