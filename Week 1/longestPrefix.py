class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #todo1: Find shortest string & select that to be my word
        if not strs:
            return ""
        
        shortest = min(strs, key = len) #find shortest string w/ key 'len'!!!
        
        for x in range(0, len(shortest)):
            for val in strs:
                if shortest[x] != val[x]:
                    return shortest[:x]
        return shortest
                