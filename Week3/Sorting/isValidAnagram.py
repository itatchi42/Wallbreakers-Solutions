from collections import Counter
class Solution:
	# Runtime: O(n)	
    def isAnagram(self, s: str, t: str) -> bool:
        cS = Counter(s)
        cT = Counter(t)
        return cS == cT
        