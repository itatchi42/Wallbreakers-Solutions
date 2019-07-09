# Runtime: O(m*n), m = #root letters, n = len(longest word) 

class Trie:
    def __init__(self):
        self.root = {} # Put class var inside __init__ to ensure it's init per test, not per process
    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr: # If char not already in trie
                curr[char] = {} # Add to trie and make space for next char
            curr = curr[char] # Advance ptr
        curr['*'] = True # Add end of word flag

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char] 
        if '*' not in curr: # False if not whole word match
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True # Return true if all letters in trie, but not whole word match
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
