# Unsure why Leetcode says my code fails the following test:
    # ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
    # It reports that my answer is 'ewqz', but the actual answer is 'yodn'
    # So I used the exact array above as a testcase and my code output 'yodn'...

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Runtime: O(n^2)
        words.sort() # Sort in ascending lexographical order
        words = words[::-1] # Reverse it (largest words first)
        
        maxCount, ans, trie = 0, '', Trie()
        
        # Put all words in trie
        for word in words:
            trie.insert(word)
        
        # Find longest word
        for word in words: 
            count = trie.search(word)
            if count >= maxCount:
                maxCount = count
                ans = word
        return ans  
        
        
class Trie:
    root = {}
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {} # Make space for next trie node
            curr = curr[char] # Shift ptr right one
        curr['*'] = True # Set ending marker
    
    def search(self, word):
        curr, count = self.root, 0
        for char in word:
            if '*' in curr: # Increm if found gestalt whole word in trie
                count += 1
            curr = curr[char] # Shift ptr right one
        return count