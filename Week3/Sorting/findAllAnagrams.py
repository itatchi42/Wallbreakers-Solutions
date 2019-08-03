from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # New approach: sliding window, O(n^2)
        cS, cP = Counter(s[ : len(p)]), Counter(p)
        res = []
        for x in range(len(s) - len(p) + 1):
            if cS == cP:
                res.append(x)
            # Advance window
            if cS[s[x]] > 1: cS[s[x]] -= 1 # Decrem if greater than 1
            else: del cS[s[x]] # Delete if already 0
            cS.update(s[x+len(p) : x+len(p)+1]) # To avoid over-indexing issue, O(n)
        return res
                    
        
        
        
    
    # Runtime: O(n^2), passes 34/36 test cases b/c Time Limit Exceeded
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     if not s: return None
    #     if len(p)  > len(s): return None
    #     res, start = [], False
    #     cS, cP = Counter(), Counter(p)
    #     indx = 0
    #     while indx < len(s):
    #         for x in range(indx, len(s)):
    #             if not cP[s[x]] or cS[s[x]] > cP[s[x]]: # Divergent
    #                 break
    #             if not start : start = True # if flag set and letter in cP
    #             if start: cS[s[x]] += 1 # Add to cS if start
    #             if cS == cP: break
    #         if cS == cP: res.append(indx)
    #         start = False
    #         cS.clear() # Reset
    #         indx += 1
    #     return res