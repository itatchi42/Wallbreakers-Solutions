from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        #Runtime: O(n)
        if not A or not B:
            return 
        #make dict of both words containing occurences
        dictA, dictB = dict(), dict()
        for wordA in A.split(' '):
            if wordA not in dictA:
                dictA[wordA] = 1
            else:
                dictA[wordA] += 1
        for wordB in B.split(' '):
            if wordB not in dictB:
                dictB[wordB] = 1
            else:
                dictB[wordB] += 1
        
        #go thru keys that have val 1
        final = []
        for kA in dictA:
            if dictA[kA] == 1 and kA not in dictB:
                print(kA)
                final.append(kA)
        for kB in dictB:
            if dictB[kB] == 1 and kB not in dictA:
                print(kB)
                final.append(kB)
        return final
        
        #optimized collections method, Runtime: O(n)
        # count = Counter(A.split(' ')) + Counter(B.split(' '))
        # return [k for k in count if count[k] == 1]
                
        