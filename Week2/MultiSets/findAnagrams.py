from collections import Counter
# import bisect
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Multiset solution:
        lenS, lenP, res = len(s), len(p), []
        cS, cP = Counter(s[ : lenP]), Counter(p)
        if not s or lenS < lenP:
            return []
        for i in range(lenS):
            if cS == cP: 
                res.append(i)
            if cS[s[i]] > 1: 
                cS[s[i]] -= 1  
            else:
                del cS[s[i]] #Remove chars w/ count 0
            #slide window right 1
            cS.update(s[i + lenP : i + lenP + 1]) #used this notation to bypass overindexing
        return res
        
        #Set solution (using bisect to insert into sorted list):
        # lenP, res = len(p), []
        # if not s or len(s) < lenP:
        #     return []
        # sortedP, sortedS = sorted(p), sorted(s[: lenP])
        # for i in range(len(s)):
        #     if sortedS == sortedP:
        #         res.append(i)
        #     if sortedS:
        #         sortedS.remove(s[i])
        #     if s[i + 1 : i + lenP + 1]: #if not adding empty str to set
        #         bisect.insort(sortedS, s[i + lenP : i + lenP + 1])
        # return res