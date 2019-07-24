class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # My soln (O(n))
        if not s and not t: return True
        if not t: return False
        if not s: return True
        
        countS, countT = Counter(s), Counter(t) # This line is bottleneck
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if not countT[s[i]]: # O(1)
                return False
            if s[i] == t[j]: 
                i += 1 # Next letter in 's'
            j += 1 # Next letter in 't'
        if i < len(s): return False
        return True
        
#     # Slower solution (O(n^2)):
#         for x in range(0, len(s)):
#             if t.find(s[x]) != -1:
#                 t = t[t.index(s[x]) + 1 : ]
#             else:
#                 return False
#         return True
                
        
        
        
#First pass (brute force, O(n^2)):        
  
        
        #         #todo check if either are null:
#         if not s and t:
#             return True
#         if s and not t:
#             return False
#         if not s and not t:
#             return True
        
#         #make sure that all of s in actually contained in t
#         setS = set(s)
#         setT = set(t)
#         if len(setS & setT) != len(setS):
#             return False
        
#         #two pointers method, one pts at curr char in s, and another pts @ curr char in t
#         begin = t.index(s[0])
#         match = ''
#         prevT = -1
#         for sPtr in range(0, len(s)): #for each char in small string
#             begin = max(begin, t.index(s[sPtr]))
#             #print(begin)
#             for tPtr in range(begin, len(t)): #for each char in long string
#                 if s[sPtr] == t[tPtr] and prevT < tPtr:
#                     prevT = tPtr
#                     #print(prevT)
#                     match += s[sPtr] #append string
#                     #print(match)
#                     break
#         if match != s:
#             return False
#         return True
